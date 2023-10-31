#Code Smells Example for long method
# calculate the total price of the item after discount
def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            total = total + discount(item.price)
    return total
    
# Get the unit price with discount
def discount(price):
    #Setting the baseline for discounts
    discontLine = 100
    if price > discontLine:
        price = price * 0.9 #10% off
        return price
    else:
        price = price * 0.95 #5% off
        return price
