import os
import sys
import imageio_ffmpeg
import yt_dlp

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    bundle_dir = sys._MEIPASS
    ffmpeg_path = os.path.join(bundle_dir, "ffmpeg-win-x86_64-v7.1.exe") 
    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

def download_media():
    ffmpeg_location = imageio_ffmpeg.get_ffmpeg_exe()
    
    url = input("Enter the YouTube URL: ")
    format_choice = input("Download as (mp3/mp4): ").lower()

    ydl_opts = {
        'ffmpeg_location': ffmpeg_location,
    }

    if format_choice == 'mp4':
        print("Downloading and converting to mp4...")
        
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4'
        })
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print("Download and conversion to mp4 completed.")
        
    elif format_choice == 'mp3':
        print("Downloading and converting to mp3...")
        
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', 
            }]
        })
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        print("Download and conversion to mp3 completed.")
        
    else:
        print("Invalid format. Please choose 'mp3' or 'mp4'.")

if __name__ == "__main__":
    download_media()