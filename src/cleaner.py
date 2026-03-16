import csv
from .logger import logging
from datetime import datetime



def parse_date(date_str: str) -> str | None:
    date_str = date_str.strip().replace('/','-')
    formats=['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y']
    
    for fmt in formats:
        
        try:
            dt_obj=datetime.strptime(date_str,fmt)
            return dt_obj.strftime("%Y-%m-%d")
        except ValueError:
            continue
    logging.error(f"Date parsing failed for '{date_str}'")
    return None

def clean_row(row: list[str], discard_writer, date_columns: int | None) -> list[str] | None:
    d1 = [_.strip() for _ in row]
    
    if "" in d1:
        logging.error(f"Null value found in row and removed: {row}")
        discard_writer.writerow(row)
        return None
    if date_columns is not None and date_columns < 1:
        logging.error(f"Date column index must be >= 1, got {date_columns}")
        return
    if date_columns is not None:
        try:
            field_to_check = d1[date_columns-1]    # Converts 1-based to 0-based
            standardized_date= parse_date(field_to_check)
            if standardized_date:
                d1[date_columns-1] = standardized_date
            else:
                discard_writer.writerow(row)
                return None
        except IndexError:
            logging.error(f"Index {date_columns} is out of range for row: {row}")
            discard_writer.writerow(row)
            return None
            
    
    return d1

def read_csv(input_path, output_path="data/Updated_file.csv", 
             discarded_path="data/discarded_data.csv", date_columns=None):
    try:
        with open(input_path, "r", newline='') as file:
            csv_read = csv.reader(file)
            try:
                header=next(csv_read)
            except StopIteration:
                logging.error("The input file is empty.")
                return
            
            
            with open(output_path, "w", newline='') as w_file, \
                 open(discarded_path, "w", newline='') as d_file:
                
                csv_w = csv.writer(w_file, delimiter=",")
                csv_discard = csv.writer(d_file, delimiter=",")
                csv_w.writerow(header)
                csv_discard.writerow(header)
                
                for line in csv_read:
                    cleaned = clean_row(line, csv_discard , date_columns)
                    if cleaned:
                        csv_w.writerow(cleaned)
    except Exception as e:
        logging.error(f"File error: {e}")

if __name__ == "__main__":
    read_csv("data.csv")
