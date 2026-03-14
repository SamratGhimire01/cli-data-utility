import csv
def read_csv(data):
    with open(data, "r",newline='') as file:
        csv_read = csv.reader(file)
        with open("Updated_file.csv","w") as w_file:
            csv_w = csv.writer(w_file, delimiter=",")
            for line in csv_read:
                d1=[_.strip() for _ in line]
                if "" in d1:
                    del line
                    continue
                csv_w.writerow(d1)
        
        
if __name__ == "__main__":
    read_csv("data.csv")