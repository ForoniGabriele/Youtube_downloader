import yt_dlp
from args import argument_parser
import os 

args = argument_parser()

def download(url = args.link, dir = args.dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

    options = {
        'outtmpl': os.path.join(dir, '%(title)s.%(ext)s'),
        'quiet': False,  # Mostra il progresso
        'no_warnings': False,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'
    }

    if 'music.' in url:
        options['format'] = 'bestaudio[ext=m4a]/best'
    
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"\n Errore durante il download: {e}")
    


download()