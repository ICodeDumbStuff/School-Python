#Prices
p_adult = 19.99
p_child = 8.99
p_fee = 2.50

#Sub Funct
def ticketprice(adult, child):

    #Total Calculation
    t_adult = adult * p_adult
    t_child = child * p_child
    total_1 = t_adult + t_child + p_fee
    total = round(total_1, 2)
    return total

adults = int(input("how many adult\n-> "))
childs = int(input("how many child\n-> "))

print("Your Total Is: £", ticketprice(adults, childs))