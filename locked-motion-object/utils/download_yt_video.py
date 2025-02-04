import yt_dlp

def download_youtube_shorts(url, output_path="."):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save as video title
        'format': 'mp4'  # Download as MP4
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download completed!")
    except Exception as e:
        print("Error:", e)

# Example usage
shorts_url = ""
download_youtube_shorts(shorts_url)
