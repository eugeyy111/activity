class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

# Creating car objects
car1 = Car("yamaha", "Mio", 2024)
car2 = Car("honda", "Xrm", 2023)

# Displaying car details
car1.display_info()
car2.display_info()