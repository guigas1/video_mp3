# YouTube para MP3

Script simples em Python para baixar o áudio de vídeos do YouTube e convertê-lo para o formato MP3.

O projeto utiliza o `yt-dlp` para realizar o download do áudio e o `FFmpeg` para fazer a conversão para `.mp3`.

## Funcionalidades

- Recebe um link de vídeo do YouTube
- Baixa automaticamente o melhor áudio disponível
- Converte o arquivo para MP3
- Salva os arquivos em uma pasta `downloads`
- Evita baixar playlists inteiras acidentalmente
- Compatível com Linux e Windows

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

Caso o comando `pip` não funcione, tente:

```bash
python -m pip install -U yt-dlp
```

No Windows, também pode ser necessário usar:

```powershell
py -m pip install -U yt-dlp
```

## Instalando o FFmpeg

O FFmpeg é necessário para converter o áudio baixado para MP3.

### Arch Linux

```bash
sudo pacman -S ffmpeg
```

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows

No Windows, uma das formas mais simples é utilizando o `winget`.

Abra o PowerShell ou Terminal do Windows e execute:

```powershell
winget install Gyan.FFmpeg
```

Depois da instalação, feche o terminal e abra novamente.

Verifique se o FFmpeg foi instalado corretamente:

```powershell
ffmpeg -version
```

E:

```powershell
ffprobe -version
```

Se os comandos mostrarem informações sobre a versão instalada, o FFmpeg está pronto para ser utilizado.

## Como usar

### Linux

Execute:

```bash
python youtube_mp3.py
```

Em algumas distribuições pode ser necessário usar:

```bash
python3 youtube_mp3.py
```

### Windows

Abra o PowerShell ou Prompt de Comando na pasta do projeto e execute:

```powershell
python youtube_mp3.py
```

Caso o comando `python` não funcione, tente:

```powershell
py youtube_mp3.py
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

O áudio será baixado e convertido automaticamente para MP3.

## Estrutura

Após executar o programa, a estrutura ficará parecida com:

```text
youtube-mp3/
├── youtube_mp3.py
├── README.md
├── requirements.txt
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

## Dependências

O arquivo `requirements.txt` pode conter:

```text
yt-dlp
```

Para instalar todas as dependências:

### Linux

```bash
pip install -r requirements.txt
```

ou:

```bash
python3 -m pip install -r requirements.txt
```

### Windows

```powershell
pip install -r requirements.txt
```

ou:

```powershell
py -m pip install -r requirements.txt
```

## Atualizando o yt-dlp

Como o YouTube altera seus mecanismos internos com frequência, pode ser necessário atualizar o `yt-dlp`.

### Linux

```bash
pip install -U yt-dlp
```

### Windows

```powershell
py -m pip install -U yt-dlp
```

## Possíveis problemas

### FFmpeg não encontrado

Caso apareça um erro parecido com:

```text
ERROR: Postprocessing: ffprobe and ffmpeg not found
```

significa que o FFmpeg não foi encontrado pelo sistema.

Confirme executando:

```bash
ffmpeg -version
```

Se o comando não funcionar, instale o FFmpeg seguindo as instruções correspondentes ao seu sistema operacional.

### Python não encontrado no Windows

Se aparecer uma mensagem indicando que `python` não foi encontrado, tente:

```powershell
py --version
```

Se funcionar, utilize `py` no lugar de `python`.

Exemplo:

```powershell
py youtube_mp3.py
```

## `.gitignore`

É recomendado criar um arquivo `.gitignore` para evitar que músicas baixadas sejam enviadas para o GitHub:

```text
downloads/
__pycache__/
*.pyc
```

## Tecnologias utilizadas

- Python
- yt-dlp
- FFmpeg

## Compatibilidade

O projeto foi pensado para funcionar em:

- Windows 10
- Windows 11
- Arch Linux
- Ubuntu
- Debian
- Outras distribuições Linux com Python e FFmpeg instalados

## Uso responsável

Este projeto foi criado para fins educacionais e pessoais.

Utilize-o apenas para baixar conteúdos que você tenha autorização para baixar ou conteúdos cuja licença permita download e uso.

O usuário é responsável por respeitar direitos autorais e os termos das plataformas utilizadas.

## Licença

Este projeto pode ser utilizado e modificado livremente para fins pessoais e educacionais.
