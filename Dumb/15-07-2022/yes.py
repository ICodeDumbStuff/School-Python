import json

#car_prices = {"Audi R8":25000, "BMW Mini":18000} # Keep commented out for reference :)

def check(car):
    if car in car_prices:
        quest = input("Would you like to remove this car? (y/n)\n-> ")
        if quest == "y":
            car_prices.pop(car, None)
            return "Deleted!"
        else:
            return car_prices[car]
    else:
        quest = input("Car not found!\nWould you like to add to the list? (y/n)\n-> ")
        if quest == "y":
            price = int(input("Whats the price\n-> "))
            car_prices[car] = price

            f = open("carsData.txt", "w")
            x = json.dumps(car_prices)
            f.write(x)
            f.close()

# Main program
while True:

    f = open("carsData.txt")
    x = f.read()
    car_prices = json.loads(x)
    f.close()

    vehicle = input("Car Name\n-> ")
    res = check(vehicle)
    print(res)
    print(car_prices)