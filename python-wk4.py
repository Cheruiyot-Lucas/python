Assignment 1: Design Your Own Class
# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage  
        self.battery = battery  
        self.powered_on = False

    # Method to power on/off
    def power(self, state):
        self.powered_on = state
        return f"{self.device_info()} is now {'ON' if state else 'OFF'}"

    # Method to install an app
    def install_app(self, app_name):
        if self.powered_on:
            return f"Installing {app_name} on {self.device_info()}..."
        else:
            return f"Cannot install apps, {self.device_info()} is OFF."

# Create smartphone objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
phone2 = Smartphone("Apple", "iPhone 15", 128, 4200)

print(phone1.power(True))
print(phone1.install_app("WhatsApp"))
print(phone2.install_app("Instagram"))

Activity 2: Polymorphism Challenge!

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        return " Driving on the road..."

class Plane(Vehicle):
    def move(self):
        return " Flying in the sky..."

class Boat(Vehicle):
    def move(self):
        return " Sailing on water..."

# List of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism
for v in vehicles:
    print(v.move())
