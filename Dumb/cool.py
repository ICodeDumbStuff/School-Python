select = int(input("number do brrrrrr\n-> "))

if select == 1:# Challenge one
    def say_hello ():

        # Say hello

        print("Hello ")

    say_hello()


elif select == 2:# Challenge Two
    def calc_square (x, y):

        #calculate the area of a square

        area = x * y
        return area

    side1 = int(input("Please enter side1 "))
    side2 = int(input("Please enter side2 "))
    total_area = calc_square(side1, side2)
    print(total_area)


elif select == 3:# Challenge Three
    def add_numbers (x,y):
        #Add two numbers together

        total = x + y
        total

    def multiply_numbers (x, y):

        #Multiply two numbers together

        total = x * y
        return total

    num1 = int(input("Please enter number1 "))
    num2 = int(input("Please enter number2 "))



    result1 = add_numbers(num1, num2)
    result2 = multiply_numbers(num1,num2)



    print("The result of adding is", result1, "and multiplying is ", result2, "")