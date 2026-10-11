import argparse
from pathlib import Path
import random
import time
import re

from transcript_store import backfill, parse_episodes, read_individuals, rebuild_exports, write_episode

BASE_URL = "https://rationalreminder.ca/podcast/"
OUTPUT_FOLDER = "transcripts"

def fetch_episode_transcript(episode_number):
    import requests
    from bs4 import BeautifulSoup

    url = f"{BASE_URL}{episode_number}"
    print(f"Fetching episode {episode_number}: {url}")
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=30)
        
        if response.status_code == 404:
            print(f"Episode {episode_number} not found (404).")
            return None

        response.raise_for_status()

    except Exception as e:
        print(f"Failed to fetch episode {episode_number}: {e}")
        raise

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the H2 tag that says "Read the Transcript" (with or without ":")
    transcript_h2 = None
    for h2 in soup.find_all('h2'):
        if re.match(r'Read the Transcript:?', h2.get_text(strip=True), re.IGNORECASE):
            transcript_h2 = h2
            break

    if not transcript_h2:
        print(f"No transcript header found for episode {episode_number}. Skipping.")
        return None

    # Collect all <p> tags after the <h2> until the next heading or end of section
    transcript = []
    current_tag = transcript_h2.find_next_sibling()

    while current_tag:
        if current_tag.name and current_tag.name.startswith('h'):
            # Stop if we hit another heading (h1, h2, etc.)
            break
        if current_tag.name == 'p':
            text = current_tag.get_text(strip=False)
            if text:
                transcript.append(text+"\n")
        current_tag = current_tag.find_next_sibling()

    if not transcript:
        print(f"No transcript content found for episode {episode_number}. Skipping.")
        return None

    return '\n'.join(transcript)

def check_for_latest_episode(episode_number):
    import requests

    # Try next to see if hit max episode
    url = f"{BASE_URL}{episode_number+1}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers, timeout=30)
    
    if response.status_code == 404:
        print(f"Episode {episode_number+1} not found (404). Likely surpassed latest episode.")
        return True
    response.raise_for_status()
    print(f"Episode {episode_number+1} found. Continuing search.")
    return False

def main():
    parser = argparse.ArgumentParser(description="Scrape individual Rational Reminder transcripts")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--backfill", action="store_true", help="Recover missing individual files from all.md; no network access")
    modes.add_argument("--rebuild", action="store_true", help="Regenerate all.md and grouped files from individuals; no network access")
    parser.add_argument("--output-dir", type=Path, default=Path(OUTPUT_FOLDER))
    args = parser.parse_args()
    folder = args.output_dir
    if args.backfill:
        backfill(folder)
        return
    if args.rebuild:
        rebuild_exports(folder)
        return

    existing = read_individuals(folder)
    if (folder / "all.md").exists():
        # Refuse to silently replace an unmigrated collection with a partial set.
        combined = parse_episodes((folder / "all.md").read_text(encoding="utf-8"))
        if set(combined) - set(existing):
            raise ValueError("Individual episodes are missing; run with --backfill first")
    if existing:
        # Recover compatibility exports after an interrupted previous run.
        rebuild_exports(folder)
    print(f"Loaded {len(existing)} individual episodes")
    downloaded = []
    downloaded_file = Path("/tmp/downloaded_episodes.txt")
    downloaded_file.write_text("", encoding="utf-8")
    episode_number = max(existing, default=0) + 1
    try:
        while True:
            transcript = fetch_episode_transcript(episode_number)
            if transcript:
                write_episode(folder, episode_number, transcript)
                downloaded.append(str(episode_number))
                print(f"Saved individual episode {episode_number}")
            elif check_for_latest_episode(episode_number):
                print(f"No more episodes found after {episode_number - 1}.")
                break
            episode_number += 1
            time.sleep(random.uniform(0.2, 3.5))
    finally:
        downloaded_file.write_text(", ".join(downloaded), encoding="utf-8")
        if read_individuals(folder):
            rebuild_exports(folder)
    print(f"Downloaded episodes: {', '.join(downloaded) or 'none'}")


if __name__ == "__main__":
    main()
