class Cat :
  def __init__(self, name, age):
    self._name = name
    self._age = age

  def info(self):
    print(f'I am a cat. My name is {self._name}. And I am {self._age} years old.')

  def sound(self):
    print("Meow")


class Dog :
  def __init__(self, name, age):
    self._name = name
    self._age = age

  def info(self):
    print(f'I am a dog. My name is {self._name}. And I am {self._age} years old.')

  def sound(self):
    print("Woof")

def main():
    cat1 = Cat("Kitty", 3.5)
    dog1 = Dog("Rex", 4)

    for animal in (cat1,dog1):
        animal.sound()
        animal.info()

if __name__ == "__main__":
    main()