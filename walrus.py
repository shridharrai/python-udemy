value = 10
# remainder = value % 3

# if remainder:
#     print(f"{value} not divisible by 3")

# if remainder := value % 3:
#     print(f"{value} is not divisible by 3")

flavors = ['Masala', 'Ginger']

while (flavor := input("Enter your flavor: ")) not in flavors:
    print(f"Sorry {flavor} is not available!")

print(f"Your choice {flavor}")
