# YouTube para MP3

Script simples em Python para baixar o áudio de vídeos do YouTube e convertê-lo para o formato MP3.

O projeto utiliza o `yt-dlp` para realizar o download do áudio e o `FFmpeg` para fazer a conversão para `.mp3`.

## Funcionalidades

- Recebe um link de vídeo do YouTube
- Baixa automaticamente o melhor áudio disponível
- Converte o arquivo para MP3
- Salva os arquivos em uma pasta `downloads`
- Evita baixar playlists inteiras acidentalmente
- Compatível com Linux

## Requisitos

Antes de executar o projeto, você precisa ter instalado:

- Python 3
- pip
- yt-dlp
- FFmpeg

## Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Entre na pasta do projeto:

```bash
cd SEU-REPOSITORIO
```

Instale o `yt-dlp`:

```bash
pip install -U yt-dlp
```

### Instalar FFmpeg

No Arch Linux:

```bash
sudo pacman -S ffmpeg
```

No Ubuntu/Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

Verifique se o FFmpeg foi instalado corretamente:

```bash
ffmpeg -version
```

E:

```bash
ffprobe -version
```

## Como usar

Execute o script:

```bash
python youtube_mp3.py
```

O programa solicitará o link do vídeo:

```text
========================================
      YouTube para MP3
========================================

Cole o link do vídeo:
```

Cole o link desejado e pressione `Enter`.

Exemplo:

```text
https://www.youtube.com/watch?v=XXXXXXXXXXX
```

O áudio será baixado e convertido automaticamente.

## Estrutura

Após executar o programa, a estrutura ficará parecida com:

```text
youtube-mp3/
├── youtube_mp3.py
├── README.md
└── downloads/
    └── Nome da música.mp3
```

Os arquivos MP3 ficam armazenados dentro da pasta:

```text
downloads/
```

## Exemplo

```text
Cole o link do vídeo: https://www.youtube.com/watch?v=XXXXXXXXXXX

Baixando...

[download] 100%

Download concluído!
Arquivo salvo em: downloads/
```

Resultado:

```text
downloads/
└── Castles in the Air.mp3
```

## Tecnologias utilizadas

- Python
- yt-dlp
- FFmpeg

## Observações

O YouTube pode alterar seus mecanismos internos com o tempo. Caso ocorram erros durante o download, tente atualizar o `yt-dlp`:

```bash
pip install -U yt-dlp
```

## Uso responsável

Este projeto foi criado para fins educacionais e pessoais.

Utilize-o apenas para baixar conteúdos que você tenha autorização para baixar ou conteúdos cuja licença permita download e uso.

O usuário é responsável por respeitar os direitos autorais e os termos das plataformas utilizadas.

## Licença

Este projeto pode ser utilizado e modificado livremente para fins pessoais e educacionais.
