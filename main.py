name = input("Enter customer name: ")
item1 = input("Enter name of item 1: ")
price1 = int(input("Enter price of item 1 (KZT): "))
item2 = input("Enter name of item 2: ")
price2 = int(input("Enter price of item 2 (KZT):"))
people = int(input("Enter number of people: "))


subtotal = price1 + price2
tip = subtotal * 0.10
total = subtotal + tip
per_person = total / people
print("=" * 30)
print("CAFE BILL")
print("=" * 30)

print("Customer :", name)
print(item1, ":", price1, "KZT")
print(item2, ":", price2, "KZT")

print("-" * 30)

print("Subtotal :", subtotal, "KZT")
print("Tip (10%) :", tip, "KZT")
print("Total :", total, "KZT")
print("Per person :", per_person, "KZT")

print("=" * 30)
print("Tip included:", tip > 0)
print("Bill over 5000 KZT:", total > 5000)
