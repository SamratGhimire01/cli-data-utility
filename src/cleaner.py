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
        return datetime.strptime(date_str.strip(),"%Y-%m-%d")
    except Exception as e:
        logging.error(f"Date error: {e}")
        return None
def clean_row(row):
    d1 = [_.strip() for _ in row]
    if "" in d1:
        logging.error(f"Null value found in row and removed: {row}")
        return None
    return d1

def read_csv(data):
    with open(data, "r",newline='') as file:
        csv_read = csv.reader(file)
        with open("Updated_file.csv","w") as w_file:
            csv_w = csv.writer(w_file, delimiter=",")
            for line in csv_read:
                d1=clean_row(line)
                if d1 is None:
                    continue
                csv_w.writerow(d1)
        
        
if __name__ == "__main__":
    read_csv("data.csv")