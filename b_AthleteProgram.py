import b_AthleteClass as ac

generic_athlete = ac.Athlete(6,220,0.2) ## instance of superclass

quarterback = ac.Football_Player(6.2,250,0.15,'quarterback','offense') ## instance of subclass


print("The height for the generic athlete is:",generic_athlete.get_ht())

#print("The team of the generic athlete is:",generic_athlete.get_team())
        ## get_team is associated with subclass and not the superclass
        ## generic_athlete is superclass
        ## superclass CANNOT accept methods of the subclass
        ## subclass CAN accept methods of the superclass
        
print("The weight for the football player is:",quarterback.get_wt())

print("The position of the football player is:",quarterback.get_position())

