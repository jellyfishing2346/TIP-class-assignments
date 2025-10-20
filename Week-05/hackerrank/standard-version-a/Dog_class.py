class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.pets_received = 0

    def receive_pet(self):
        self.pets_received += 1
        return f"{self.name} has received a pet!"

    def bark(self):
        return f"{self.name} says woof!"

# Create Dog objects
dog1 = Dog("Buddy", "Poodle")
dog2 = Dog("Bella", "Labrador")

# Dog Interactions
print(dog2.bark())
print(dog1.receive_pet())
print(dog2.receive_pet())
print(dog1.pets_received)
print(dog2.pets_received)
# Output: Bella says woof! 
# Output: Buddy has received a pet!
# Output: Bella has received a pet!
# Output: 1
# Output: 1