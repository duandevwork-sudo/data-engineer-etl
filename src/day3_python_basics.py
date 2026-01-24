#“Built a Python ETL script to process CSV sales data

import csv 

file_path  = "data/sales.csv"

total_revenue = 0
count = 0
max_value = 0
high_revenue = 0
low_revenue = 0

with open(file_path, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader: 
        order_id = int(row["order_id"])
        price = int(row["price"])
        quantity = int(row["quantity"])
        
        total_price = price * quantity
        
        #total_revenue
        total_revenue += total_price
        
        #count
        count += 1
        
        #max_value
        if total_price > max_value:
            max_value = total_price
        
        #hight_revenue & low_revenue 
        if total_price > 300:
            high_revenue += total_price
        else:
            low_revenue += total_price
        
        
        print(f"Order {order_id} - Total: {total_price}")
average = total_revenue / count

print("Total Revenue", total_revenue)
print("Count", count)
print("Max Value", max_value)
print(f"Average: {average:.2f}")
print("High Revenue", high_revenue)
print("Low Revenue", low_revenue)
