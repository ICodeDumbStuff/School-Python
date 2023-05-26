import json

f = open("Data/savesData.txt")
x = f.read()
test = json.loads(x)
f.close()
print(test[hi])
print("Done :)")