users = [
    {'total': 100, 'coupon': 'P20'},
    {'total': 200, 'coupon': 'P30'}
]

discounts = {
    'P20': (0.2, 0),
    'P30': (0, 30)
}

for user in users:
    percent, fixed = discounts.get(user['coupon'], (0, 0))
    discount = user['total'] * percent + fixed
    print(f"Discount is {discount}")