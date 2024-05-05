#Jonas Dupaya
class Galleria:
    def __init__(self, location, stores):
        self.location = location
        self.stores = stores

    def Status(self):
        return("location: " + self.location + "we have 3 stores:" + "\n" + self.stores)
    
    def __del__(self):
        print("Galleria got deleted.")

class ShoeShop:
    def __init__(self, brand, age, location, stores):
        self.brand = brand 
        self.age = age
        self.subject = Galleria(location, stores)

    def inside(self):
        return self.subject.Status()
    
    def __del__(self):
        print("ShoeShop got deleted")

test = ShoeShop("Nike", "8-40", "Iloilo \n", "> Fashion Feet\n> Albertos\n> Happy Feet")
print(test.inside())
del test
del Galleria
        

