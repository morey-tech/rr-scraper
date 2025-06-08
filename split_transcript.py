import os
import re

INPUT_FILE = "rational_reminder_transcripts.md"
OUTPUT_FOLDER = "transcripts"

def split_transcripts():
    # Ensure the output folder exists
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Input file '{INPUT_FILE}' not found.")
        return

    # Split the content into episodes using the "## Episode N" header as a delimiter
    episodes = re.split(r"(## Episode \d+)", content)
    print(len(episodes))
    
    # The first element may be empty or unrelated content, so we skip it
    episodes = episodes[1:]

    # Process episodes in pairs: header and content
    for i in range(0, len(episodes), 2):
        if i + 1 >= len(episodes):
            break
        header = episodes[i].strip()
        body = episodes[i + 1].strip()

        # Extract the episode number from the header
        match = re.match(r"## Episode (\d+)", header)
        if not match:
            print(f"Skipping malformed header: {header}")
            continue

        episode_number = match.group(1)
        output_file = os.path.join(OUTPUT_FOLDER, f"episode_{episode_number}.md")

        # Write the episode content to a separate file
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.write(f"{header}\n\n{body}")

        print(f"Saved Episode {episode_number} to {output_file}")

if __name__ == "__main__":
    split_transcripts()