# main.py
from downloader import download_audio
from transcriber import transcribe_audio
from summarizer import summarize_text

def main():
    url = input("Cole a URL do vídeo do YouTube: ")
    audio_path = download_audio(url)
    print("✅ Áudio baixado e convertido!")

    transcription = transcribe_audio(audio_path)
    print("✅ Transcrição feita com sucesso!")

    summary = summarize_text(transcription)
    print("✅ Resumo:")
    print(summary)

if __name__ == "__main__":
    main()
