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
        
        """ 
        Sells a bike 
        Adds to the shops profit by subtracting the price the bike is being
        sold at from the cost to manufacture the bike
        The bike is then removed from the inventory of the bikeshop
        """
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
        """
        Buys a bike, subtracts the price the bike is being sold at from the
        customer's fund.
        Bike is then appended to the garage array to store the bike
        Method ends buy printing the sold bike's model
        """
        self.fund -= 1.2*(bike.cost)
        self.garage.append(bike)
        print("\n" +bike.model)
    
