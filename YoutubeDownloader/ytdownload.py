import yt_dlp

def download_video(video_url, download_path='.'):
    # Simplified options to avoid separate video/audio merging
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save with video title
        'format': 'best[ext=mp4]/best',  # Choose the best single (progressive) format
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Download completed! Saved to {download_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    video_url = input("Enter the Youtube video URL: ")
    download_path = input("Enter the path to save the video (default is current directory): ")
    if not download_path:
        download_path = '.'
    download_video(video_url, download_path)
