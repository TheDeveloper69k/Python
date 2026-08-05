import os

print("Current Working Directory: ", os.getcwd())
print("Absolute Path of tut.txt: ", os.path.abspath("tut.txt"))

file = open("tut.txt", "a")

file.write("\nYOU CANNOT ESCAPE YOUR FATE")
file.close()

f = open("tut.txt", "r")
data = f.read()
print(data)
f.close()