import yt_dlp
import os 
import re

def progress_hook(d, progress_callback=None):
    if d['status'] == 'finished':
        if progress_callback:
            progress_callback(100)
    
    elif d['status'] == 'downloading':
        if '_percent_str' in d and progress_callback:
            cleaned_percent_str = re.sub(r'\x1b\[.*?m', '', d['_percent_str'])
            p = float(cleaned_percent_str.strip().replace(',', '.').strip('%'))
            progress_callback(p)


def download(url, dir, progress_callback=None):
    if not os.path.exists(dir):
        os.makedirs(dir)

    options = {
        'outtmpl': os.path.join(dir, '%(title)s.%(ext)s'),
        'quiet': False,  # Mostra il progresso
        'no_warnings': False,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'progress_hooks': [lambda d: progress_hook(d, progress_callback)],
    }

    if 'music.' in url:
        options['format'] = 'bestaudio[ext=m4a]/best'
    
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
            return True
    except Exception as e:
        print(f"\n Errore durante il download: {e}")
        return str(e)
