seat_type = input("Enter seat type: ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper")
    case "ac":
        print("AC")
    case _:
        print("Invalid")