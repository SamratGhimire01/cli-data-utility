from argparse import ArgumentParser

def get_args():
    
    parse = ArgumentParser(description="CSV Cleaning and Date Parsing Tool")
    parse.add_argument("--input", required=True, help="Path to the input CSV file" )
    parse.add_argument("--output", default="Updated_file.csv", help="Path to save the cleaned CSV" )
    parse.add_argument("--dfile", default="discarded_data.csv", help="Path to save the discarded CSV" )
    return parse.parse_args()

