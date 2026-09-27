import os
import yt_dlp


def baixar_mp3(url):
    pasta_saida = "downloads"

    # Cria a pasta caso não exista
    os.makedirs(pasta_saida, exist_ok=True)

    opcoes = {
        # Baixa o melhor áudio disponível
        "format": "bestaudio/best",

        # Nome do arquivo
        "outtmpl": os.path.join(
            pasta_saida,
            "%(title)s.%(ext)s"
        ),

        # Converte para MP3 usando FFmpeg
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],

        # Evita baixar playlist inteira sem querer
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            print("\nBaixando...\n")
            ydl.download([url])

        print("\nDownload concluído!")
        print(f"Arquivo salvo em: {pasta_saida}/")

    except Exception as erro:
        print("\nOcorreu um erro:")
        print(erro)


def main():
    print("=" * 40)
    print("      YouTube para MP3")
    print("=" * 40)

    url = input("\nCole o link do vídeo: ").strip()

    if not url:
        print("Nenhum link informado.")
        return

    baixar_mp3(url)


if __name__ == "__main__":
    main()