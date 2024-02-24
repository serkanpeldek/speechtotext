import os
from  utils.download_audio import download_audio
from utils.files import save_text_to_file
from utils.openai_funcs import transcritp_with_wisper, generate_corrected_transcript
from utils.prompts import system_prompt_anly, system_prompt_pro


if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=wXYx6iJNqMc'
    audio_path = download_audio(video_url, output_path='downloads', file_name='sales')
    
    transcript = transcritp_with_wisper(audio_path)
    transcript_prof = generate_corrected_transcript("gpt-4-turbo-preview", 0, system_prompt_pro, transcript)
    transcript_anly = generate_corrected_transcript("gpt-4-turbo-preview", 0, system_prompt_anly, transcript_prof)
    
    save_text_to_file(transcript, "downloads", "sales_transcript")
    save_text_to_file(transcript_prof, "downloads", "sales_transcript_prof")
    save_text_to_file(transcript_anly, "downloads", "sales_transcript_anly")
