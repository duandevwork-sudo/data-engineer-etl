# Day 1 - Python Basics for Data Engineer

print("Hello Data Engineer!")

numbers = [1, 2, 3, 4, 5]

total = 0
for n in numbers:
    total += n

print("Total:", total)

def square(x):
    return x * x

print("Square of 5:", square(5))

high_revenue = 0
low_revenue = 0

revenue_all = 0
revenue_q2 = 0
sales = [
    {"order_id": 1,"price": 100, "quantity": 2},
    {"order_id": 2,"price": 200, "quantity": 1},
    {"order_id": 3,"price": 150, "quantity": 3},
]

count = 0
max_value = 0

for item in sales :
    total_price = item["price"] * item["quantity"]
    
    revenue_all += total_price
    
    #lession1 
    if item["quantity"] >= 2 :
        revenue_q2 += total_price
        
    #lession2
    count += 1
    
    #lession3
    if total_price > max_value:
        max_value = total_price
        
    #lession5
    if total_price > 300:
        high_revenue += total_price
    else:
        low_revenue += total_price
    
    print(f"Order {item['order_id']} - Total: {total_price}")
        
print("Total Revenue:", revenue_all)
print("Revenue >= 2:", revenue_q2)
print("Count", count)
print("Max Value", max_value)

#lesson4 

average = revenue_all / count
print(f"Average: {average:.2f}")

#lesson5
print("Hight Revenue", high_revenue)
print("Low Revenue",low_revenue)





#lesson 1 
#BÀI 1 – TÍNH TỔNG CÓ ĐIỀU KIỆN (CỰC QUAN TRỌNG)
#Yêu cầu - Chỉ tính doanh thu của các đơn có quantity ≥ 2

#//    revenue_q2 = 0
#//    if item["quantity"] >= 2 :
#//        revenue_q2 += total_price
    
#lesson 2 – ĐẾM SỐ ĐƠN HÀNG
#Yêu cầu - Đếm xem có bao nhiêu đơn hàng

#//     count = 0
#//     count += 1

#lesson 3 – TÌM ĐƠN CÓ GIÁ TRỊ CAO NHẤT

#//     max_value = 0
#//     if total_price > max_value:
#//        max_value = total_price

#lesson 4 – TÍNH DOANH THU TRUNG BÌNH / ĐƠN

#//     average = 0;
#//     average = revenue_all / count
#//     print(f"Average: {average:.2f}")

#lesson 5 – GROUP THEO LOGIC (NÂNG NÃO NHẸ)

#//     high_revenue = 0
#//     low_revenue = 0
#//     if total_price > 300:
#//             high_revenue += total_price
#//         else:
#//             low_revenue += total_price   
#//         print(f"Order {item['order_id']} - Total: {total_price}")