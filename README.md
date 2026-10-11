# Rational Reminder transcript scraper

Individual files in `transcripts/individual/episode_N.md` are the source of truth.
Each contains an episode heading followed by the original transcript, including
speaker labels and paragraph boundaries. Existing unpadded filenames are retained.
`transcripts/all.md` and `transcripts/groups_of_20/` are compatibility exports.

## Backfill existing episodes without fetching the podcast site

```bash
python3 main.py --backfill
python3 main.py --rebuild
python3 -m unittest discover -p 'test_*.py' -v
```

`--backfill` reads the saved `all.md`, checks every existing individual transcript
for conflicts, creates only missing files, and verifies the complete collection.
It does not request any transcripts from the website or modify `all.md`. Gaps in
episode numbering remain gaps; an episode must already have saved text to be
backfilled. A conflicting individual file stops the migration before any writes.
Repeated runs do not change files that already match.

Parsing removes whitespace around each transcript body; internal text, punctuation,
Unicode characters, speaker labels, and paragraph boundaries are preserved.
The existing 362 individual files are retained unchanged; the initial backfill
adds 62 files for the 424 episodes already present in `all.md`, through episode 430.

`--rebuild` regenerates the combined and grouped views from individuals, using
numeric episode order and groups of 20 available episodes. Group names reflect
their actual first and last episode numbers. It removes obsolete generated group
filenames after writing replacements. An already equivalent `all.md` retains its
historical formatting. Both commands and the tests use only the Python standard
library and require no model, database, or network access. `--output-dir` selects
an alternate transcript directory.

## Scrape new episodes

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

The normal run reads the individual files, starts after their highest episode
number, and saves each fetched episode individually before rebuilding the
compatibility exports. Files are replaced atomically; unchanged files are left
alone. If interrupted, a subsequent run rebuilds exports from saved individuals.
An incomplete migration is rejected with instructions to run `--backfill`.

HTTP failures abort the run instead of being treated as missing transcripts;
requests have a 30-second timeout. Missing pages or pages without transcript text
retain the existing next-episode discovery behavior. The scraper does not yet
revisit older episodes for corrections or delayed transcripts; this change does
not fill historical gaps by guessing or fabricating content.

The [GitHub Actions workflow](.github/workflows/update_transcripts.yml) runs on
Fridays at 08:00 UTC and supports manual dispatch. It runs the tests, scrapes, and
commits changed transcript files, preserving Git history for ingestion consumers.
