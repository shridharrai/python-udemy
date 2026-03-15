amount = int(input("Enter order amount: "))

delivery_fees = 0 if amount > 300 else 20

print(f"Delivery fees is: {delivery_fees}")