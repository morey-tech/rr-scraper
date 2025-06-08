import random
import requests
from bs4 import BeautifulSoup
import time
import re

BASE_URL = "https://rationalreminder.ca/podcast/"
OUTPUT_FILE = "rational_reminder_transcripts.md"

def fetch_episode_transcript(episode_number):
    url = f"{BASE_URL}{episode_number}"
    print(f"Fetching episode {episode_number}: {url}")
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch episode {episode_number}: {e}")
        return None

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


def main():
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Rational Reminder Episodes\n\n")

        for episode_number in range(1, 361):
            transcript = fetch_episode_transcript(episode_number)
            if transcript:
                f.write(f"## Episode {episode_number}\n")
                f.write(f"{transcript}\n\n")
            
            # Be polite to the server
            sleep_time = random.uniform(0.2, 3.5)  # Random delay between 200ms and 3.5s
            print(f"Sleeping for {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)

    print(f"\nDone! Transcripts saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
