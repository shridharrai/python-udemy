import sys
from decimal import Decimal

# Mutable
sugar_amount = 2
# print(f"Initial Sugar: {sugar_amount}")
sugar_amount = 12
# print(f"Updated Sugar: {sugar_amount}")

# print(f"Id of 2: {id(2)}")
# print(f"Id of 12: {id(12)}")

# Immutable
spice_mix = set()
# print(f"Spice is: {spice_mix}")
# print(f"Spice Id is: {id(spice_mix)}")
spice_mix.add("Ginger")
spice_mix.add("Cardamon")
# print(f"Update Spice is: {spice_mix}")

num_one = 10
num_two = 3
res = num_one / num_two
res_two = num_one // num_two
# print(f"Res of division is: {res}")
# print(f"Res without decimal is: {res_two}")

base = 2
pow = 4
expon = base ** pow
# print(f"Exponential is: {expon}")

big_num = 1_000_000_000
# print(f"Big num is: {big_num}")

ideal_temp = 95.3
current_temp = 95.499999999999999999999999999999999
# print(f"Diff is: {current_temp - ideal_temp}")
# print(sys.float_info)

my_name = "Shridhar Rai"
print(f"My name is: {my_name[0:8:1]}")
print(f"My name is: {my_name[0:8:2]}")
print(f"My reverse name is: {my_name[::-1]}")
