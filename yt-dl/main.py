import youtube_dl

def download_video(url, opt={}):
    ydl_opts = opt
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = "https://www.youtube.com/watch?v=Pih7_kWWM8o"

ydl_opts = {
    'format': 'bestaudio/best',
    'verbose': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

download_video(video_url, opt={})