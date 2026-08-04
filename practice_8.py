def temp_Convertor():
    choice = input("Enter 'C' To convert Celsius to Fahrenheit , Kelvin or 'F' to convert Fahrenheit to Celsius , Kelvin or 'K' to convert Kelvin to Celsius , Fahrenheit : ")

    if choice == 'C':
        Celsius = float(input("Enter The Tempuratire in Celsius :"))
        Fahrenheit = (Celsius * 9/5) + 32
        Kelvin = Celsius + 273.15
        print(f"Temperature in Fahrenheit: {Fahrenheit}")
        print(f"Temperature in Kelvin: {Kelvin}")

    elif choice == 'F':
        Fahrenheit = float(input("Enter The Tempuratire in Fahrenheit :"))
        Celsius = (Fahrenheit - 32) * 5/9
        Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
        print(f"Temperature in Celsius: {Celsius}")
        print(f"Temperature in Kelvin: {Kelvin}")

    else :
        Kelvin = float(input("Enter The Tempuratire in Kelvin :"))
        Celsius = Kelvin - 273.15
        Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
        print(f"Temperature in Celsius: {Celsius}")
        print(f"Temperature in Fahrenheit: {Fahrenheit}")

temp_Convertor()
