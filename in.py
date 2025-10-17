# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return "Some generic animal sound"
    
    def move(self):
        return f"{self.name} is moving"
    
    def __str__(self):
        return f"{self.name} ({self.species})"

# Child class
class Cat(Animal):
    def __init__(self, name, breed, indoor=True):
        super().__init__(name, "Felis catus")  # Call parent constructor
        self.breed = breed
        self.indoor = indoor
    
    # Method overriding
    def speak(self):
        return "Meow!"
    
    # Additional method
    def purr(self):
        return "Purrrrr..."

# Another child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canis familiaris")
        self.breed = breed
    
    def speak(self):
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball"

# Usage
cat = Cat("Whiskers", "Siamese")
dog = Dog("Buddy", "Golden Retriever")

print(cat.speak())  # Output: Meow!
print(dog.speak())  # Output: Woof!
print(cat.move())   # Output: Whiskers is moving
print(dog.fetch())  # Output: Buddy is fetching the ball
