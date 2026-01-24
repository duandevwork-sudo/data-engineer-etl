import csv 

file_path  = "data/sales.csv"

with open(file_path, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for i, row in enumerate(reader): 
        print(row)
        if i == 9:  # in 10 dòng
            break
