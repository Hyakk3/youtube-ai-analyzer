# transcriber.py
import os
from dotenv import load_dotenv
import openai

load_dotenv()  # Carrega as variáveis do .env

# Cria o cliente com sua chave da OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return response.text
