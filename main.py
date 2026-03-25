from src.cleaner import read_csv
from src.cli import get_args
from src.logger import logging

def main():
    
    args = get_args()
    logging.info("CSV Cleaner started with args: %s", args)
    read_csv(args.input, args.output, args.dfile, args.date)
    
if __name__ == "__main__":
    main()
