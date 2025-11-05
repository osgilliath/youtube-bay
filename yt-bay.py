import os

def download_video():
    url = input("Enter the YouTube URL: ")
    format = input("Download as (mp3/mp4): ").lower()

    if format == 'mp4':
        os.system(f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" {url}')
    elif format == 'mp3':
        os.system(f'yt-dlp -x --audio-format mp3 {url}')
    else:
        print("Invalid format. Please choose 'mp3' or 'mp4'.")

if __name__ == "__main__":
    download_video()