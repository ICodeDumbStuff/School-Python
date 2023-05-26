def validate_car(miles, age):
  if miles >= 0 and miles < 10000 and age >= 0 and age <= 5:
    return True
  else:
    return False

miles = int(input("Enter the number of miles driven: "))
age = int(input("Enter the age of the car in years: "))

if validate_car(miles, age):
  print("Valid data entered")
else:
  print("Invalid data entered")
