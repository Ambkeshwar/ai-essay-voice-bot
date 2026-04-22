import subprocess
import tempfile
from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


async def transcribe_audio(file):
    # Read uploaded file
    audio_bytes = await file.read()

    if not audio_bytes:
        raise ValueError("Empty audio file")

    # Save original file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename) as input_file:
        input_file.write(audio_bytes)
        input_path = input_file.name

    # Create temp wav file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as output_file:
        output_path = output_file.name

    # Convert to WAV using ffmpeg
    command = [
        "C:\\Users\\Ambkeshwar.shukla\\Desktop\\ffmpeg.exe",
        "-i", input_path,
        "-ar", "16000",        # sample rate (recommended)
        "-ac", "1",            # mono channel
        "-y",                  # overwrite
        output_path
    ]

    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Send WAV file to OpenAI
    with open(output_path, "rb") as f:
        response = client.audio.transcriptions.create(
            model="gpt-4o-transcribe",
            file=("audio.wav", f)
        )

    return response.text