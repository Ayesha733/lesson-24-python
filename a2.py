class vehicle:
    def __init__(self, name,max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

audi = vehicle("Audi",240, 18)
print("Model Name:",audi.name)
print("Model Max Speed:" ,audi.max_speed)
print("Model Mileage:" , audi.mileage)
print("\n")
        

BMW = vehicle("BMW",240, 15)
print("Model Name:",BMW.name)
print("Model Max Speed:" ,BMW.max_speed)
print("Model Mileage:" , BMW.mileage)
print("Model Mileage:",BMW.mileage)
        