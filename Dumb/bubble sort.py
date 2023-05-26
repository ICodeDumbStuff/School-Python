array = [4,3,1,9,5,7,2,8,6]
print(array)
x = len(array)
for y in range(x):
    for i in range(x-1):
        a1 = array[i]
        a2 = array[i+1]
        if a1 > a2:
            array[i+1] = a1
            array[i] = a2
print(array)