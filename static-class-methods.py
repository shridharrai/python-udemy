class ChaiOrder:
    def __init__(self, tea_type, sweet, size):
        self.type = tea_type
        self.sweet = sweet
        self.size = size

    @staticmethod
    def is_valid_size(size):
        return size in ['small', 'medium', 'large']

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweet"],
            order_data["size"]
        )

is_valid = ChaiOrder.is_valid_size("large")
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweet": "medium", "size": "large"})
order2 = ChaiOrder("Ginger", "high", "small")

print(is_valid)
print(order1.__dict__)
print(order2.__dict__)