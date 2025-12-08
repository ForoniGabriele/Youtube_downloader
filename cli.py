from download import download
from args import argument_parser
import sys

def main():
    """Funzione principale"""
    try:
        args = argument_parser()
        
        success = download(
            url=args.link,
            dir=args.dir
        )
        
        # Exit code appropriato
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n\n Operazione annullata")
        sys.exit(1)


if __name__ == '__main__':
    main()
