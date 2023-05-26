f = open("file.txt", "a")
for i in range(100000000):
    f.write(f"{i}, ")
f.close()
print("done")