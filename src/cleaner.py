import csv
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.ERROR, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("log.log"),
        logging.StreamHandler()
    ]
)

def parse_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d")
    except Exception as e:
        logging.error(f"Date error for '{date_str}': {e}")
        return None

def clean_row(row, discard_writer):
    d1 = [_.strip() for _ in row]
    
    if "" in d1:
        logging.error(f"Null value found in row and removed: {row}")
        discard_writer.writerow(row)
        return None
        
    for field in d1:
        if "-" in field and len(field) == 10:
            parsed = parse_date(field)
            if not parsed:
                logging.error(f"Invalid date format in field '{field}' : '{row}'")
                discard_writer.writerow(row)
                return None
    return d1

def read_csv(input_path, output_path="Updated_file.csv"):
    try:
        with open(input_path, "r", newline='') as file:
            csv_read = csv.reader(file)
            
            
            with open(output_path, "w", newline='') as w_file, \
                 open("discarded_data.csv", "w", newline='') as d_file:
                
                csv_w = csv.writer(w_file, delimiter=",")
                csv_discard = csv.writer(d_file, delimiter=",")
                
                for line in csv_read:
                    cleaned = clean_row(line, csv_discard)
                    if cleaned:
                        csv_w.writerow(cleaned)
    except Exception as e:
        logging.error(f"File error: {e}")

if __name__ == "__main__":
    read_csv("data.csv")
