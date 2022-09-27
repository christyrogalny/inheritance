
class Plant:
    def __init__(self,color):
        self.__color = color #one attribute


    def get_color(self): # one method called get_color
        return self.__color 


class Flower(Plant): ## sub class to 'Plant' which is the superclass
    def __init__(self,color, petals): ## first do the __init__ method of Plant
        Plant.__init__(self,color) ## to create Plant superclass we pass on the color

        self.__petals = petals

    def get_petals(self):
        return self.__petals

