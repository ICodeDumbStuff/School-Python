def age_height ():
    age = int(input("Please enter your age: "))
    height = int(input("Please enter your height: "))
    if age < 10 and  height > 150:
        return True
    return False

def cost ():
    child = int(input("How many children will be riding today? "))
    adult = int(input("How many adults will be riding today? "))
    if child > 0:
        for i in range (child):
            result = age_height()
            if result == "False":
                return "Sorry, you do not fit the age and height requirements. "
    if child > 1 and adult > 1:
        return "Ticket cost is £12"
    cost = (child * 2.50) + (adult * 4.50)
    return f"Ticket cost is {cost}"

result = cost()
print(result)