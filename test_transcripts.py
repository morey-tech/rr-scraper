import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import main
from transcript_store import backfill, parse_episodes, read_individuals, rebuild_exports, write_episode


class TranscriptTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.folder = Path(temporary.name)
        self.enterContext(contextlib.redirect_stdout(io.StringIO()))

    def combined(self, text):
        path = self.folder / "all.md"
        path.write_text(text, encoding="utf-8")
        return path

    def snapshot(self):
        return {str(p.relative_to(self.folder)): (p.read_bytes(), p.stat().st_mtime_ns)
                for p in self.folder.rglob("*.md")}

    def run_main(self, *args):
        with patch("sys.argv", ["main.py", "--output-dir", str(self.folder), *args]):
            main.main()

    def test_backfill_preserves_source_existing_files_and_speaker_text(self):
        body = "Host: Why?\n\nGuest: A café, ‘quote’, and a nonbreaking\u00a0space."
        source = self.combined(f"# Rational Reminder Episodes\n\n## Episode 1\n{body}\n\n## Episode 3\nSecond answer.\n")
        write_episode(self.folder, 1, body)
        before = self.snapshot()
        self.assertEqual(backfill(self.folder), [3])
        self.assertEqual(read_individuals(self.folder), {1: body, 3: "Second answer."})
        self.assertEqual(self.snapshot()["all.md"], before["all.md"])
        self.assertEqual(self.snapshot()["individual/episode_1.md"], before["individual/episode_1.md"])
        self.assertEqual(source.read_bytes(), before["all.md"][0])
        after = self.snapshot()
        self.assertEqual(backfill(self.folder), [])
        self.assertEqual(self.snapshot(), after)

    def test_backfill_conflict_fails_before_writing_missing_files(self):
        self.combined("## Episode 1\nOriginal\n## Episode 2\nSecond")
        write_episode(self.folder, 1, "Edited individually")
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "conflict"):
            backfill(self.folder)
        self.assertEqual(self.snapshot(), before)

    def test_backfill_rejects_individual_not_in_source(self):
        self.combined("## Episode 1\nOriginal")
        write_episode(self.folder, 2, "Only here")
        with self.assertRaisesRegex(ValueError, "conflict"):
            backfill(self.folder)

    def test_invalid_source_is_rejected_without_writes(self):
        for source in ("No headings", "## Episode 1\n", "## Episode 1\nA\n## Episode 1\nB", "Lost content\n## Episode 1\nA"):
            with self.subTest(source=source):
                self.combined(source)
                with self.assertRaises(ValueError):
                    backfill(self.folder)
                self.assertFalse((self.folder / "individual").exists())

    def test_heading_must_be_on_its_own_line(self):
        body = "Host: We mentioned ## Episode 123 before.\n## Episode 99 discussion\nGuest: Yes."
        self.assertEqual(parse_episodes("## Episode 1\n" + body), {1: body})

    def test_mismatched_individual_heading_is_rejected(self):
        directory = self.folder / "individual"
        directory.mkdir()
        (directory / "episode_1.md").write_text("## Episode 2\nWrong", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "does not match"):
            rebuild_exports(self.folder)
        self.assertFalse((self.folder / "all.md").exists())

    def test_exports_sort_numerically_group_twenty_and_remove_stale_ranges(self):
        numbers = [1, *range(3, 24)]
        for n in reversed(numbers):
            write_episode(self.folder, n, f"Speaker: Body {n}")
        rebuild_exports(self.folder)
        groups = self.folder / "groups_of_20"
        self.assertEqual(sorted(p.name for p in groups.glob("*.md")), [
            "episodes_00001_to_00021.md", "episodes_00022_to_00023.md"])
        combined = parse_episodes((self.folder / "all.md").read_text())
        self.assertEqual(list(combined), numbers)
        for p in groups.glob("*.md"):
            for n, body in parse_episodes(p.read_text()).items():
                self.assertEqual(body, combined[n])
        write_episode(self.folder, 24, "New episode")
        rebuild_exports(self.folder)
        self.assertFalse((groups / "episodes_00022_to_00023.md").exists())
        self.assertTrue((groups / "episodes_00022_to_00024.md").exists())
        before = self.snapshot()
        rebuild_exports(self.folder)
        self.assertEqual(self.snapshot(), before)

    def test_editing_individual_rebuilds_both_exports(self):
        write_episode(self.folder, 1, "Old")
        rebuild_exports(self.folder)
        write_episode(self.folder, 1, "Corrected")
        rebuild_exports(self.folder)
        for p in [self.folder / "all.md", *self.folder.glob("groups_of_20/*.md")]:
            self.assertEqual(parse_episodes(p.read_text()), {1: "Corrected"})

    def test_cli_backfill_and_rebuild_never_scrape(self):
        self.combined("## Episode 1\nSource")
        with patch.object(main, "fetch_episode_transcript", side_effect=AssertionError("Network used")):
            self.run_main("--backfill")
            self.run_main("--rebuild")

    def test_normal_run_writes_individual_first_and_recovers_after_failure(self):
        write_episode(self.folder, 1, "Existing")
        downloaded = self.folder / "downloaded.txt"
        original_path = Path
        def runtime_path(value):
            return downloaded if value == "/tmp/downloaded_episodes.txt" else original_path(value)
        with patch.object(main, "Path", side_effect=runtime_path), patch.object(main.time, "sleep"), \
                patch.object(main, "fetch_episode_transcript", side_effect=["New speaker: Answer", RuntimeError("HTTP failure")]) as fetch:
            with self.assertRaisesRegex(RuntimeError, "HTTP failure"):
                self.run_main()
            self.assertEqual([c.args[0] for c in fetch.call_args_list], [2, 3])
        self.assertEqual(read_individuals(self.folder)[2], "New speaker: Answer")
        self.assertEqual(parse_episodes((self.folder / "all.md").read_text())[2], "New speaker: Answer")
        self.assertEqual(downloaded.read_text(), "2")
        # A later invocation recovers a source written before an interrupted export.
        write_episode(self.folder, 3, "Recovered")
        with patch.object(main, "Path", side_effect=runtime_path), \
                patch.object(main, "fetch_episode_transcript", return_value=None) as fetch, \
                patch.object(main, "check_for_latest_episode", return_value=True):
            self.run_main()
            fetch.assert_called_once_with(4)
        self.assertEqual(parse_episodes((self.folder / "all.md").read_text())[3], "Recovered")

    def test_normal_run_refuses_partial_migration(self):
        self.combined("## Episode 1\nOld\n## Episode 2\nMissing individual")
        write_episode(self.folder, 1, "Old")
        with patch.object(main, "fetch_episode_transcript", side_effect=AssertionError("Network used")):
            with self.assertRaisesRegex(ValueError, "backfill"):
                self.run_main()


if __name__ == "__main__":
    unittest.main()
