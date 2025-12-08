import argparse

def argument_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l',
        '--link',
        type = str,
        required = True,
        help = 'URL del video / canzone da scaricare'
    )

    parser.add_argument(
        '-d',
        '--dir',
        type = str,
        default = './Yt_downloader',
        help = 'Cartella di destinazione dei download',
    )

    args = parser.parse_args()
    
    return args
