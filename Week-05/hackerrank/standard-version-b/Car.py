class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

    def age(self, current_year):
        return current_year - self.year
    
cars1 = Car("Toyota", "Camry", 2010)
cars2 = Car("Honda", "Civic", 2015)

print(cars2.description())  # Output: 2015 Honda Civic
print(cars1.age(2024))      # Output: 14