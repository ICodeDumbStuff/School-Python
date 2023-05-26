'''
price
if over 120
give 25% disc
'''
#funct
def pricething(price):
    if price > 120:
        if price > 200 and price < 500:
            return price * 0.50
        return price * 0.75
    else:
        return price
price1 = int(input("Price\n-> "))
returningstuff = pricething(price1)
print(f'£{returningstuff}')