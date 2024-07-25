import sys
from pathlib import Path
from openai import OpenAI
import os
import openai
from dotenv import load_dotenv


def main(folder_name):
    # Load the environment variables
    load_dotenv()
    openai.api_key = os.environ["OPENAI_API_KEY"]
    client = OpenAI()

    # Path to the text file
    solution_file_path = Path(__file__).parent / f"{folder_name}/audios.txt"
    if not solution_file_path.is_file():
        print(f"Error: {solution_file_path} does not exist.")
        return

    # Open the text file and read lines
    with open(solution_file_path, "r") as file:
        lines = file.readlines()

    # Path to save the MP3 files
    base_path = Path(__file__).parent / f"{folder_name}/audios"
    base_path.mkdir(parents=True, exist_ok=True)

    # Loop through each line and create a separate MP3 file
    for i, line in enumerate(lines):
        # Ensure non-empty lines are processed
        if line.strip():
            speech_file_path = base_path / f"line_{i+1}.mp3"
            response = client.audio.speech.create(
                model="tts-1-hd", voice="alloy", input=line
            )
            response.stream_to_file(speech_file_path)
            print(f"Saved {speech_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder-name>")
    else:
        folder_name = sys.argv[1]
        main(folder_name)
