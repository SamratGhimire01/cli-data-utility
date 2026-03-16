from src.cleaner import read_csv
from src.cli import get_args

def main():
    print("CSV Cleaner running")
    args = get_args()
    
    read_csv(args.input, args.output, args.date)
    
if __name__ == "__main__":
    main()
