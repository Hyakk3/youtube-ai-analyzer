from pytubefix import YouTube
import ffmpeg
import os


def download_audio(url: str, output_path='downloads') -> str:
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    print(f"Baixando: {yt.title}")
    m4a_path = audio_stream.download(output_path=output_path, filename='audio.m4a')
    mp3_path = os.path.join(output_path, 'audio.mp3')

    # Converter com FFMPEG
    ffmpeg.input(m4a_path).output(mp3_path).run(overwrite_output=True)
    os.remove(m4a_path)

    return mp3_path