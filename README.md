
# Audio Transcription and Analysis

This repository contains Python scripts for downloading audio from a YouTube video, transcribing it using OpenAI's models, and generating corrected transcripts for both professional and analytical purposes.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/serkanpeldek/speechtotext.git
   cd speechtotext
   ```

2. **Create and activate a Conda environment:**
   ```bash
   conda create --name your-env-name
   conda activate your-env-name
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the main script:**
   ```bash
   python stt.py
   ```

2. The script will download audio from the specified YouTube video, transcribe it using OpenAI's model, and generate corrected transcripts for professional and analytical purposes.

3. The transcripts will be saved in the `downloads` folder with filenames:
   - `sales_transcript.txt` (original transcript)
   - `sales_transcript_prof.txt` (professional corrected transcript)
   - `sales_transcript_anly.txt` (analytical corrected transcript)

## File Structure

- `utils/`: Contains utility functions for downloading audio, file operations, OpenAI functions, and system prompts.
- `script.py`: The main script that orchestrates the entire process.
- `requirements.txt`: List of Python packages required for the project.

## Acknowledgments

- OpenAI Docs: https://platform.openai.com/docs/overview

## Note

Make sure to comply with OpenAI's usage policies and guidelines when using the GPT-4 Turbo model.


