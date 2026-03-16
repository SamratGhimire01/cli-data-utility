from src.cleaner import read_csv
from src.cli import get_args
from src.logger import logging

def main():
    logging.info("CSV Cleaner started with args: %s", args)
    args = get_args()
    
    read_csv(args.input, args.output, args.dfile, args.date)
    
if __name__ == "__main__":
    main()
