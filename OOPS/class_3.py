class Animal:

    Choice = input("Enter the animal name: Dog or Cat !\n")

    def make_sound(self):
        if(self.Choice == "Dog"):
            print("Bark")
        elif(self.Choice == "Cat"):
            print("Meow")
        else:
            print("Unknown Animal Sound")

    def greet(self):
        print(f"Hello, I am a {self.Choice}.")

    @staticmethod
    def static_method():
        print("This is a static method.") #No need to give self in parameters to call this method

Hiten = Animal()
Hiten.make_sound()
Hiten.greet()
Hiten.static_method()
