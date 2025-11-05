
import os
import imageio_ffmpeg

def download_media():
    ffmpeg_location = imageio_ffmpeg.get_ffmpeg_exe()
    url = input("Enter the YouTube URL: ")
    format = input("Download as (mp3/mp4): ").lower()

    if format == 'mp4':
        print("Downloading and converting to mp4...")
        os.system(f'yt-dlp --ffmpeg-location "{ffmpeg_location}" -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" --merge-output-format mp4 {url}')
        print("Download and conversion to mp4 completed.")
    elif format == 'mp3':
        print("Downloading and converting to mp3...")
        os.system(f'yt-dlp --ffmpeg-location "{ffmpeg_location}" -x --audio-format mp3 {url}')
        print("Download and conversion to mp3 completed.")
    else:
        print("Invalid format. Please choose 'mp3' or 'mp4'.")

if __name__ == "__main__":
    download_media()
