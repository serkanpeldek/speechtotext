from openai import OpenAI

def transcritp_with_wisper(audio_path):
    client = OpenAI()

    audio_file= open(audio_path, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
    )
    return transcript

def generate_corrected_transcript(model, temperature, system_prompt, transcript):
    client = OpenAI()
    response = client.chat.completions.create(
        model= model,
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcript
            }
        ]
    )
    return response.choices[0].message.content