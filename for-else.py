staff = [('Shri', 26), ('Adi', 22)]

for name, age in staff:
    if age >= 30:
        print(f"{name} is eligible")
        break
else:
    print(f"Inside else if loop doesn't break")