import streamlit as st
from yt_dlp import YoutubeDL
import os

def download_youtube_video(url, output_path="."):
    try:
        ydl_opts = {
            'format': 'best',  # Seleciona o melhor formato disponível que já inclui vídeo e áudio
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Template para o nome do arquivo de saída
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)  # Obtém o caminho do arquivo baixado

        st.success("Download concluído!")
        return file_path
    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
        return None

# Criação da interface com Streamlit
st.title("Download videos from youtube")

# Entrada para a URL do vídeo
video_url = st.text_input("URL video: ")

# Entrada para o caminho do diretório de saída
output_directory = st.text_input("keep this / mantenha assim: ", ".")

# Botão para iniciar o download
if st.button("Download video"):
    if video_url:
        video_path = download_youtube_video(video_url, output_directory)
        if video_path:
            # Disponibiliza o vídeo para download
            with open(video_path, "rb") as file:
                btn = st.download_button(
                    label="Click here to download video",
                    data=file,
                    file_name=os.path.basename(video_path),
                    mime="video/mp4"
                )
    else:
        st.warning("Por favor, insira uma URL válida do YouTube. / Please put a valid URL from yotube")
