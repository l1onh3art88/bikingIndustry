#Creates a bike shop with 6 bicycle models and charges bikes at 20% over its cost.
#Creates three customers with $200, $500, and $1000 respectively.
#Prints the name of each customer and the bikes each person can afford. 
#Prints initial inventory
#Each customer buys a bike, prints name of bike, the cost, and how much money
#the customer has in his fund
#After a purchase, the bike shop prints the remaining inventory and how much
#the bike shop has made

from bicycles import Bicycle
from bicycles import BikeShop
from bicycles import Customer


if __name__ == '__main__': 

#Creates a bike shop with 6 bicycle models and charges bikes at 20% over its cost.
    b1 = Bicycle("Aero", 20, 100)
    b2 = Bicycle("TCR Advanced", 20, 380)
    b3 = Bicycle("Trinity", 20, 600)
    b4 = Bicycle("Defy", 20, 130)
    b5 = Bicycle("Contend", 20, 400)
    b6 = Bicycle("Escape", 20, 800)
    
    
    bikeshop = BikeShop("Spencer's Bike Mart",  0)
    bikeshop.inventory.extend((b1,b2,b3,b4,b5,b6))
    
#Creates three customers with $200, $500, and $1000 respectively.
    p1 = Customer("Bob", 200)
    p2 = Customer("Steve", 500)
    p3= Customer("John", 1000)

    customers = [p1, p2, p3]
    
    
#Prints the name of each customer and the bikes each person can afford. 
    
    for x in customers:
        print("\nPossible bikes for " + x.name + ":\n") 
        for y in bikeshop.inventory:
            if (y.cost*1.2)<=x.fund:
                print(y.model)
                
                
#Prints initial inventory
    print("\nThese are all the bikes: \n")
    for y in bikeshop.inventory:
        print(y.model)
        
        
#Each customer buys a bike, prints name of bike, the cost, and how much money
#the customer has in his fund    

    for x in customers: 
        for y in bikeshop.inventory:
            if ( y.cost*1.2)<= x.fund:
                x.buy(y)
                bikeshop.sell(y)
                print("There are " + str(x.fund) + " dollars left in " + x.name + "'s fund")
                
    
#After a purchase, the bike shop prints the remaining inventory and how much
#the bike shop has made
    
    for y in bikeshop.inventory:
        print(y.model)
    
    bikeshop.balance()