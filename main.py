import os
import random
import requests
from bs4 import BeautifulSoup
import time
import re

BASE_URL = "https://rationalreminder.ca/podcast/"
OUTPUT_FOLDER = "transcripts"
OUTPUT_FILE = f"{OUTPUT_FOLDER}/all.md"

def fetch_episode_transcript(episode_number):
    url = f"{BASE_URL}{episode_number}"
    print(f"Fetching episode {episode_number}: {url}")
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 404:
            print(f"Episode {episode_number} not found (404).")
            return None

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

def check_for_latest_episode(episode_number):
    # Try next to see if hit max episode
    url = f"{BASE_URL}{episode_number+1}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 404:
        print(f"Episode {episode_number+1} not found (404). Likely surpassed latest episode.")
        return True
    elif response.status_code == 200:
        print(f"Episode {episode_number+1} found. Continuing search.")
        return False

def split_transcripts():
    # Define the subdirectory for groups of 20 episodes
    group_output_folder = os.path.join(OUTPUT_FOLDER, "groups_of_20")

    # Ensure the output folder exists
    if not os.path.exists(group_output_folder):
        os.makedirs(group_output_folder)

    # Clean up old group files before regenerating
    print("Cleaning up old episode group files...")
    if os.path.exists(group_output_folder):
        for old_file in os.listdir(group_output_folder):
            if old_file.startswith("episodes_") and old_file.endswith(".md"):
                old_file_path = os.path.join(group_output_folder, old_file)
                os.remove(old_file_path)
                print(f"Removed old file: {old_file}")

    try:
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Input file '{OUTPUT_FILE}' not found.")
        return

    # Split the content into episodes using the "## Episode N" header as a delimiter
    episodes = re.split(r"(## Episode \d+)", content)
    
    # The first element may be empty or unrelated content, so we skip it
    episodes = episodes[1:]

    # Combine headers and bodies into pairs
    episode_pairs = []
    for i in range(0, len(episodes), 2):
        if i + 1 >= len(episodes):
            break
        header = episodes[i].strip()
        body = episodes[i + 1].strip()
        episode_pairs.append(f"{header}\n\n{body}")

    # Write episodes into files, 20 episodes per file
    for i in range(0, len(episode_pairs), 20):
        chunk = episode_pairs[i:i + 20]

        # Extract actual episode numbers from the first and last episode in the chunk
        first_episode_match = re.search(r'## Episode (\d+)', chunk[0])
        last_episode_match = re.search(r'## Episode (\d+)', chunk[-1])

        if not first_episode_match or not last_episode_match:
            print(f"Warning: Could not extract episode numbers from chunk starting at index {i}")
            continue

        start_episode = int(first_episode_match.group(1))
        end_episode = int(last_episode_match.group(1))

        # Zero-pad the episode numbers to 5 digits
        start_episode_padded = str(start_episode).zfill(5)
        end_episode_padded = str(end_episode).zfill(5)

        output_file = os.path.join(group_output_folder, f"episodes_{start_episode_padded}_to_{end_episode_padded}.md")

        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.write("\n\n".join(chunk))

        print(f"Saved episodes {start_episode} to {end_episode} in {output_file}")

def main():
    # Read the existing file to determine which episodes are already present
    existing_episodes = set()

    # Ensure the output folder exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    try:
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r"## Episode (\d+)", line)
                if match:
                    existing_episodes.add(int(match.group(1)))
        print(f"Existing episodes: {existing_episodes}")
    except FileNotFoundError:
        print(f"{OUTPUT_FILE} not found. A new file will be created.")

    # Track episodes downloaded in the current run
    downloaded_episodes_file = "/tmp/downloaded_episodes.txt"
    downloaded_episodes = []  # Store episode numbers in a list

    with open(OUTPUT_FILE, 'a+', encoding='utf-8') as f:
        # Write the header if the file is empty
        f.seek(0)
        if not f.read().strip():
            f.write("# Rational Reminder Episodes\n\n")

        episode_number = max(existing_episodes, default=0) + 1
        while True:
            transcript = fetch_episode_transcript(episode_number)
            if transcript:
                # Write the episode header and transcript
                f.write(f"## Episode {episode_number}\n")
                f.write(f"{transcript}\n\n")
                # Add the downloaded episode to the list
                downloaded_episodes.append(str(episode_number))
            elif check_for_latest_episode(episode_number):
                print(f"No more episodes found after {episode_number - 1}.")
                break

            episode_number += 1
            # Be polite to the server
            sleep_time = random.uniform(0.2, 3.5)  # Random delay between 200ms and 3.5s
            print(f"Sleeping for {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)

    # Write the downloaded episodes to the temporary file as a comma-separated list
    with open(downloaded_episodes_file, 'w', encoding='utf-8') as tmp_file:
        tmp_file.write(", ".join(downloaded_episodes))

    print(f"\nDone! Transcripts saved to {OUTPUT_FILE}")
    print(f"Episodes downloaded during this run are logged in {downloaded_episodes_file}")
    split_transcripts()

if __name__ == "__main__":
    main()
