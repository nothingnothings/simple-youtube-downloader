import yt_dlp
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