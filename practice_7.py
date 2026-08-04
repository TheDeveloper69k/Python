def biggest(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif(c>a and c>b):
        return c
    else:
        return "All numbers are equal"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = biggest(a, b, c)
print("The biggest number is:", result)
