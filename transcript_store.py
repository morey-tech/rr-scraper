"""Individual episode storage and reproducible compatibility exports."""

from pathlib import Path
import os
import re
import tempfile


HEADING = re.compile(r"^## Episode ([1-9][0-9]*)[ \t]*$", re.MULTILINE)
FILENAME = re.compile(r"episode_([1-9][0-9]*)\.md")


def parse_episodes(text):
    """Preserve transcript text; normalize only whitespace around each body."""
    matches = list(HEADING.finditer(text))
    if not matches:
        raise ValueError("No episode headings found")
    if text[:matches[0].start()].strip() not in ("", "# Rational Reminder Episodes"):
        raise ValueError("Unexpected content before first episode")
    episodes = {}
    for i, match in enumerate(matches):
        number = int(match[1])
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[match.end():end].strip()
        if number in episodes:
            raise ValueError(f"Duplicate episode {number}")
        if not body:
            raise ValueError(f"Empty transcript for episode {number}")
        episodes[number] = body
    return episodes


def write_if_changed(path, text):
    """Publish complete files atomically and leave unchanged files alone."""
    path = Path(path)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(text)
        temporary.chmod(0o644)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return True


def read_individuals(folder):
    episodes = {}
    for path in sorted((Path(folder) / "individual").glob("episode_*.md")):
        match = FILENAME.fullmatch(path.name)
        if match is None:
            raise ValueError(f"Unexpected episode filename: {path.name}")
        number = int(match[1])
        parsed = parse_episodes(path.read_text(encoding="utf-8"))
        if set(parsed) != {number}:
            raise ValueError(f"Episode heading does not match {path.name}")
        episodes[number] = parsed[number]
    return episodes


def write_episode(folder, number, body):
    text = f"## Episode {number}\n\n{body.strip()}"
    if set(parse_episodes(text)) != {number}:
        raise ValueError(f"Unexpected episode heading inside episode {number}")
    return write_if_changed(Path(folder) / "individual" / f"episode_{number}.md", text)


def backfill(folder):
    """Recover missing individuals from all.md, never overwrite conflicts."""
    folder = Path(folder)
    source = parse_episodes((folder / "all.md").read_text(encoding="utf-8"))
    existing = read_individuals(folder)
    conflicts = [n for n, body in existing.items() if n not in source or source[n] != body]
    if conflicts:
        raise ValueError(f"Individual transcripts conflict with all.md: {sorted(conflicts)}")
    # Validate the whole input before writing anything. Retrying is safe.
    missing = sorted(set(source) - set(existing))
    for number in missing:
        write_episode(folder, number, source[number])
    if read_individuals(folder) != source:
        raise ValueError("Backfill verification failed")
    print(f"Verified {len(source)} individual episodes; created {len(missing)} missing files")
    return missing


def rebuild_exports(folder):
    folder = Path(folder)
    episodes = read_individuals(folder)
    if not episodes:
        raise ValueError("No individual transcripts; use --backfill if all.md exists")
    ordered = sorted(episodes)
    combined = folder / "all.md"
    # Preserve historical formatting when episode content is already identical.
    current = parse_episodes(combined.read_text(encoding="utf-8")) if combined.exists() else {}
    if current != episodes:
        text = "# Rational Reminder Episodes\n\n" + "".join(
            f"## Episode {n}\n{episodes[n]}\n\n" for n in ordered
        )
        write_if_changed(combined, text)
    groups = folder / "groups_of_20"
    expected = set()
    for i in range(0, len(ordered), 20):
        numbers = ordered[i:i + 20]
        name = f"episodes_{numbers[0]:05d}_to_{numbers[-1]:05d}.md"
        expected.add(name)
        write_if_changed(groups / name, "\n\n".join(
            f"## Episode {n}\n\n{episodes[n]}" for n in numbers
        ))
    # Remove obsolete generated ranges only after replacements were published.
    for path in groups.glob("episodes_*.md"):
        if path.name not in expected:
            path.unlink()
    print(f"Exported {len(episodes)} episodes into all.md and {len(expected)} grouped files")
