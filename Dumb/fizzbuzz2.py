import time
number = 1

sleep = 0

while True:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
        number = number + 1
        time.sleep(sleep)
    elif number % 3 == 0:
        print("Fizz")
        number = number + 1
        time.sleep(sleep)
    elif number % 5 == 0:
        print("Buzz")
        number = number + 1
        time.sleep(sleep)
    elif number == number:
        print(number)
        number = number + 1
        time.sleep(sleep)