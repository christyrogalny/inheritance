# This program demonstrates polymorphism.

from nis import cat
import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    gorilla = animals.Mammal('gorilla')
    dog = animals.Dog()
    cat = animals.Cat()

    '''
    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    gorilla.show_species()
    gorilla.make_sound()

    print()

    dog.show_species()
    dog.make_sound()

    print()

    cat.show_species()
    cat.make_sound()
    '''

## this instead of whats commented out above
    show_mammal_info(gorilla)
    show_mammal_info(dog)
    show_mammal_info(cat)
    show_mammal_info('bird') 


def show_mammal_info(creature): ## creature is an object
    if isinstance(creature,animals.Mammal): 
    ## this checks to see if this instance belongs to this class
        ## is bird a mammal? its a string so no
    ## this means if the creature is an instance of this class - 
    ## then carry out these instances
        creature.show_species()
        creature.make_sound()
    else:
        print(creature, 'is not a mammal')


# Call the main function.
main()

