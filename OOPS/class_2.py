class Student:
    language = "Python"  # class Attribute
    grade = 10

Hiten = Student()
Hiten.language = "Java"  # instance Attribute

print(f"{Hiten.language}\n{Hiten.grade}")

#INSTANCE ATTRIBUTE WILL OVERRIDE THE CLASS ATTRIBUTE