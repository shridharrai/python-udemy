def generate_bill(chai = 0, samosa = 0):
    """
    Calculate the total bill of customer
    """
    total = chai * 10 + samosa * 20
    return total

print(generate_bill.__doc__)
print(generate_bill.__name__)
