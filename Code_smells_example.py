#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            total = total + discount(item.price)
    return total

def discount(price):
    discontLine = 100
    if price > discontLine:
        price = price * 0.9
        return price
    else:
        price = price * 0.95
        return price
