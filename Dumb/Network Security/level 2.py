def discount(price1):
    if price1 >= 0 and price1 <= 50:
        if price1 >= 51:
            if price1 >= 101 and price1 <= 200:
                return price1 * 0.8
            else:
                return price1 * 0.85
        else:
            return price1 * 0.9
    return price1
# Main program
price = int(input("Please enter the price\n-> "))
print(f"Price: {discount(price)}")