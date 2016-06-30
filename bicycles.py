#Classes mirror the bike industry. There are 3 classes: Bicycle, Bike Shops,
#and Customers

class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        
class BikeShop(object):
    def __init__(self, name,profit):
        self.name = name
        self.inventory = []
        self.profit = profit
    
    def sell(self, bike):
        self.profit += (1.2*(bike.cost)-(bike.cost)) 
        self.inventory.remove(bike)
    
    def balance(self):
        print("The shop has made " + str(self.profit) + " dollars!")
        
class Customer(object):
    def __init__(self,name,fund):
        self.name = name
        self.fund = fund
        self.garage = []
    
    def buy(self, bike):
        self.fund -= 1.2*(bike.cost)
        self.garage.append(bike)
        print("\n" +bike.model)
    
