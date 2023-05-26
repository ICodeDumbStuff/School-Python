import random
def adder(number):
    return number + random.randint(1, 100000000)
# Main program
num = int(input("Please enter a number\n-> "))
res = adder(num)
print("Number:", res)