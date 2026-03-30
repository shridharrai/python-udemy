class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 10}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} chai not available")
        if not isinstance(cups, int):
            raise TypeError("Invalid cup type")
        total = menu[flavor] * cups
        print(f"Your bill for {flavor} chai is: {total}")
    except Exception as e:
        print("Error is: ", e)
    finally:
        print("Thank You!")

bill('mint', 2)
bill('masala', 'two')
bill('ginger', 3)