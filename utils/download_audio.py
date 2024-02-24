from pytube import YouTube
import os

def download_audio(video_url, output_path='downloads', file_name='audio'):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        # Set the complete file path
        file_name = file_name + ".mp4"
        file_path = f"{output_path}/{file_name}"
        if os.path.exists(file_path):
            print(f" {file_path} already exists")
            return file_path
        # Create a YouTube object
        youtube = YouTube(video_url)

        # Get the highest resolution audio stream
        audio_stream = youtube.streams.filter(only_audio=True).first()


        

        # Download the audio stream to the specified output path and file name
        audio_stream.download(output_path, filename=file_name)

        print(f"Download successful! Saved as: {file_path}")
    except Exception as e:
        print(f"Error: {e}")
    
    return file_path


