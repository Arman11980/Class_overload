class Buiding:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor
        
    def __bool__(self):
        return self.numberOfFloors

    def __str__(self):
        return self.buildingType

    def __eq__(self, other):
        return self.floor > other.floor

home1 = Buiding('небоскрёб',15)
home2 = Buiding('хрущёвка',5)
print(home1 == home2)