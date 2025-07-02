# summarizer.py
import openai
import os

def summarize_text(text: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que resume textos longos."},
            {"role": "user", "content": f"Resuma o seguinte texto:\n\n{text}"}
        ]
    )

    return response.choices[0].message["content"]