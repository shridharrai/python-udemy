chai_type = "ginger"  # global

def update_order():
    chai_type = "elaichi"  # local
    def kitchen():
        # nonlocal chai_type
        # global chai_type
        chai_type = "masala"  # enclosed
        print(f"Kitchen {chai_type}")
    kitchen()
    print(f"update order {chai_type}")
update_order()
print(f"global {chai_type}")