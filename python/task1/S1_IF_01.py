def shipping_cost(weight_kg, is_member):
    if weight_kg < 1:
        cost = 10
    elif weight_kg <= 5:
        cost = 20
    else:
        cost = 30

    if is_member:
        cost *= 0.8

    return cost

print(shipping_cost(0.5, True))
print(shipping_cost(3, False))
