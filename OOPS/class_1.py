class Employee:
    language = "Python" #THIS IS A CLASS ATTRIBUTE
    salary = 120

Hiten = Employee()
Hiten.name = "Hiten" #THIS IS AN INSTANCE ATTRIBUTE
Hiten.ID = 123
print(f"{Hiten.name}\n{Hiten.ID}\n{Hiten.language}\n{Hiten.salary}")

Aniket = Employee()
Aniket.name = "Aniket" #THIS IS AN INSTANCE ATTRIBUTE
Aniket.ID = 456
print(f"{Aniket.name}\n{Aniket.ID}\n{Aniket.language}\n{Aniket.salary}")