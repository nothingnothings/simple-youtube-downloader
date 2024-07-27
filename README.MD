# YouTube Video Downloader

## Overview

This Python script downloads YouTube videos from a list of URLs provided in a text file. It uses `yt-dlp`, a powerful and flexible tool for downloading videos from YouTube and other platforms, and requires `ffmpeg` for handling video and audio merging.

## Features

* Downloads videos from YouTube URLs listed in a text file.
* Saves videos in the specified directory.
* Merges video and audio into a single MP4 file if necessary.

## Installation

### 1. Install Python

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/). During installation, make sure to check the option to "Add Python to PATH".

### 2. Install `yt-dlp`

Install the `yt-dlp` package using `pip`. Open a Command Prompt or Terminal and run:

```
pip install yt-dlp
```

### 3. Install `ffmpeg`

`ffmpeg` is required for merging video and audio streams. Follow these steps to install it:

1. **Download `ffmpeg`** :

* Visit [FFmpeg&#39;s official download page](https://ffmpeg.org/download.html) and download the Windows builds from a trusted source like [Gyan.dev]().

2. **Extract the ZIP File** :

* Extract the ZIP file to a location on your computer, e.g., `C:\ffmpeg`.

3. **Add `ffmpeg` to System PATH** :

* Press `Win + X` and select `System`.
* Click on `Advanced system settings`.
* Click on `Environment Variables`.
* Under `System variables`, find the `Path` variable and click `Edit`.
* Click `New` and add the path to the `bin` directory inside the extracted `ffmpeg` folder (e.g., `C:\ffmpeg\bin`).
* Click `OK` to save and close all dialogs.

4. **Verify `ffmpeg` Installation** :

* Open Command Prompt and run:
  <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg></button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">ffmpeg -version
  </code></div></div></pre>
* You should see the version information for `ffmpeg`.

### 4. Download the Script

Save the following script as `download_youtube_videos.py`:

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

## Usage

1. **Prepare Your URL File** :

* Create a file named `youtube-urls.txt` in the same directory as your script.
* List each YouTube URL on a new line in this file.

1. **Run the Script** :

* Open Command Prompt or Terminal.
* Navigate to the directory where `download_youtube_videos.py` is located.
* Run the script with:
  <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copiar código</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python download_youtube_videos.py
  </code></div></div></pre>
* The script will read URLs from `youtube-urls.txt`, download each video, and save them in the `downloads` directory.

## Troubleshooting

* **Error: `ffmpeg` not installed** :
  Ensure `ffmpeg` is installed and added to your PATH. Verify with `ffmpeg -version`.
* **Permission Issues** :
  Make sure you have write permissions to the `downloads` directory.
* **Invalid URL** :
  Check that URLs in `youtube-urls.txt` are correct and accessible.

## License

This script is provided as-is with no warranty. Feel free to modify and use it as needed.
