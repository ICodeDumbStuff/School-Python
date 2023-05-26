# Removed initial Vars coz not needed

bal = int(input("Please enter your accounts balance")) # Cast to int
meal = int(input("Please enter the cost of your meal")) # Cast to int
def newbalance(bal,meal): # Removed New, wasnt needed
    new = bal - meal # This initilises new so no need to declare
    return new

print(newbalance(bal, meal)) # Changed order, Removed new coz wasnt needed