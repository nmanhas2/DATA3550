class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def show(self):
        print(f"I am {self._name}, and I am {self._age}")
    
    def speak(self):
        return "I don't know how to speak."

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color
    
    def speak(self):
        return "Meow"

    def show(self):
        print(f"I am {self._name}, and I am {self._age}, and I am {self._color}")

class Dog(Animal):
    def speak(self):
        return "Woof"

class Fish(Animal):
    pass

def main():
    c = Cat("Tom", 2, "black")
    c.show()
    c.speak()

    f = Fish("Nemo", 45)
    f.speak()
    
    a = Animal("Rex", 8)
    a.show()
    a.speak()

if __name__ == "__main__":
    main()

    
