def math(num1, num2):
    return num1 + num2
print(math(int(input("Number 1\n-> ")), int(input("Number 2\n-> "))))
try:
    raise FailureError("no")
except FailureError as e:
    print(e)