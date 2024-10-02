# YouTube Video Downloader

## Visão Geral
[![en](https://img.shields.io/badge/lang-en-red.svg?style=flat-square)](https://github.com/nothingnothings/simple-youtube-downloader)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg?style=flat-square)](https://github.com/nothingnothings/simple-youtube-downloader/blob/master/README.pt-br.md)

Este script em Python baixa vídeos do YouTube a partir de uma lista de URLs fornecidas em um arquivo de texto. Ele utiliza o `yt-dlp`, uma ferramenta poderosa e flexível para baixar vídeos do YouTube e outras plataformas, e requer o `ffmpeg` para a mesclagem de vídeo e áudio.


## Destaques

* Baixa vídeos de URLs do YouTube listadas em um arquivo de texto.
* Salva os vídeos no diretório especificado.

## Instalação

### 1. Instale o Python

Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/). Durante a instalação, verifique a opção para "Adicionar Python ao PATH".

### 2. Instale o `yt-dlp`

Instale o pacote `yt-dlp` usando `pip`. Abra um Prompt de Comando ou Terminal e execute:

```
pip install yt-dlp
```

### 3. Instale o `ffmpeg`

O `ffmpeg` é necessário para mesclar streams de vídeo e áudio. Siga estes passos para instalá-lo:

1. **Baixe o `ffmpeg`**:

* Visite [a página oficial de downloads do FFmpeg](https://ffmpeg.org/download.html) e baixe as versões para Windows de uma fonte confiável, como [Gyan.dev](https://www.gyan.dev/ffmpeg/).

2. **Extraia o Arquivo ZIP**:

* Extraia o arquivo ZIP para um local em seu computador, como, por exemplo, `C:\ffmpeg`.

3. **Adicione o `ffmpeg` ao PATH do Sistema**:

* Pressione `Win + X` e selecione `Sistema`.
* Clique em `Configurações avançadas do sistema`.
* Clique em `Variáveis de Ambiente`.
* Em `Variáveis do sistema`, encontre a variável `Path` e clique em `Editar`.
* Clique em `Novo` e adicione o caminho para o diretório `bin` dentro da pasta extraída do `ffmpeg` (por exemplo, `C:\ffmpeg\bin`).
* Clique em `OK` para salvar e fechar todos os diálogos.

4. **Verifique a Instalação do `ffmpeg`**:

* Abra o Prompt de Comando e execute:
```
ffmpeg -version
```

### 4. Faça o Download do Script

Salve o seguinte script como `download_youtube_videos.py`:

<pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg></button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">import yt_dlp
import os

# File path to the text file containing YouTube URLs
urls_file_path = 'youtube-urls.txt'
# Directory where files will be saved
downloads_dir = 'downloads'

# Ensure the downloads directory exists
os.makedirs(downloads_dir, exist_ok=True)

# Function to download a single video
def download_video(url):
    ydl_opts = {
        'outtmpl': os.path.join(downloads_dir, '%(title)s.%(ext)s'),  # Save video with title and appropriate extension
        'format': 'bestvideo+bestaudio/best',  # Download the best available video and audio
        'merge_output_format': 'mp4',  # Merge into MP4 if needed
        'ffmpeg_location': 'C:/path/to/ffmpeg/bin/',  # Specify the path to ffmpeg (adjust if needed)
    }
  
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Main function to handle downloading
def main():
    try:
        # Read URLs from file
        with open(urls_file_path, 'r') as file:
            urls = file.readlines()
      
        # Strip whitespace and empty lines
        urls = [url.strip() for url in urls if url.strip()]

        if not urls:
            print('No URLs found in the file.')
            return

        print(f'Found {len(urls)} URLs to download.')

        # Download each video
        for url in urls:
            print(f'Downloading video from URL: {url}')
            download_video(url)

        print('All videos downloaded successfully.')

    except Exception as e:
        print(f'Error occurred: {e}')

if __name__ == "__main__":
    main()
</code></div></div></pre>

## Utilização

1. **Prepare seu Arquivo com as URLS** :

* Crie um arquivo chamado youtube-urls.txt no mesmo diretório do seu script.
* Neste arquivo, escreva cada URL do YouTube em uma nova linha.

2. **Execute o Script** :

* Abra o Prompt de Comando ou Terminal.
* Navegue até o diretório onde download_youtube_videos.py está localizado.
* Execute o script com:
  <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg></button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python download_youtube_videos.py
  </code></div></div></pre>
* O script lerá as URLs de `youtube-urls.txt`, baixará cada vídeo e os salvará no diretório `downloads`.

## Troubleshooting

* **Error: `ffmpeg` not installed** :
  Certifique-se de que o ffmpeg está instalado e adicionado ao seu `PATH`. Verifique com o comando `ffmpeg -version`, no CMD ou terminal.
* **Permission Issues** :
  Certifique-se de que você tem permissões de gravação no diretório `downloads`.
* **Invalid URL** :
  Verifique se as URLs em `youtube-urls.txt` estão corretas e acessíveis.

## License

Este script é fornecido como está, sem garantia. Sinta-se à vontade para modificar e usá-lo conforme o necessário.
