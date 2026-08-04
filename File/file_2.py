f = open("tut.txt", "w")

f.write("Hiten Is A GOD")
f.close()

f = open("tut.txt", "r")

data = f.read()
print(data)
f.close()
