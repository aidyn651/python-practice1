# Task D1 — Multiple Orders
name = input("Enter customer name: ")

total = 0
count = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    
    if item.lower() == "done":
        break
    
    price = float(input("Enter price: "))
    total += price
    count += 1

print("Customer :", name.upper())
print("Items :", count)
print("Subtotal :", total, "KZT")


# Task D2 — Time-Based Discount
hour = int(input("Enter current hour (0-23): "))

if 6 <= hour < 12:
    discount_rate = 0.10
    label = "Morning discount"
elif 12 <= hour < 17:
    discount_rate = 0.0
    label = "No discount"
elif 17 <= hour < 22:
    discount_rate = 0.05
    label = "Evening discount"
else:
    print("Closed")
    exit()

discount = total * discount_rate
after_discount = total - discount
tip = after_discount * 0.10
final_total = after_discount + tip

print("-----------------------------")
print("Time period :", label)
print("Discount :", discount, "KZT")
print("Tip (10%) :", tip, "KZT")
print("Total :", final_total, "KZT")
print("-----------------------------")


# Task D3 — Name Analysis
print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))

if name[0].upper() == 'A' or name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")
