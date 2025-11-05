import os

def download_media():
    url = input("Enter the YouTube URL: ")
    choice = input("Download as (audio/video): ").lower()

    if choice == 'video':
        print("Downloading video...")
        os.system(f'yt-dlp -f best {url}')
        print("Video download completed.")
    elif choice == 'audio':
        print("Downloading audio...")
        os.system(f'yt-dlp -x --audio-format best {url}')
        print("Audio download completed.")
    else:
        print("Invalid choice. Please choose 'audio' or 'video'.")

if __name__ == "__main__":
    download_media()