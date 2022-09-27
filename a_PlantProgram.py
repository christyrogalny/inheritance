import a_PlantClass as pc

primrose = pc.Plant("Green") ## instance of the Plant superclass

sunflower = pc.Flower("Yellow", 20) ## creating off of Flower subclass 
## have to give the number of petals = ',20' 

print(primrose.get_color())

print(sunflower.get_color()) 
print(sunflower.get_petals()) ## get_petals belongs to the subclass so you can 
                              ## call it within the subclass


#print(primrose.get_petals()) *have to comment out so the program will work*
            ## primrose is superclass and get_petals is subclass
            ## superclass does not inherit from subclass
            ## subclass does inherit from superclass 

