# main.py
# Add import statement for vehicle class

from vehiclePackage.vehicleClass import *

if __name__ == "__main__":
    # Instantiate an object if type Vehicle
    myCorvette = Vehicle("car", 120) # Trigger a call to constructor
    myCorvette.printType()      # Invoke the method on the object
    
    # Invoke the getter for maximum speed, store the return value in a variable 
    # Print that to the console
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    
    # Instantiate another Vehicle object. You can name it
    myCorolla = Vehicle("car") #myCorolla is an object of type Vehicle
    
    
    # I want a list of 3 vehicles: car, boat, space ship
    # You can pick the names and properties
    # I want some friendly output to demo your work
    
    myVehicles = [  Vehicle("Toyota Camery", 150)
                  , Vehicle ("sailboat", 20)
                  , Vehicle ("Falcon Heavy", 4000)]
    
    # Iterate over the list
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())
    
    
    