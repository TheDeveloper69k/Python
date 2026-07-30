#IF ELIF ELSE LADDER

age = int(input("Enter a number: "))

if(age >= 18 and age <= 70):
    print("You are eligible to vote")

elif(age < 18 and age >= 0):
    print("You are not eligible to vote")

elif(age < 0):
    print("Age cannot be negative")

elif(age > 70):
    print("You are Dead Man")

else:
    print("Invalid age")