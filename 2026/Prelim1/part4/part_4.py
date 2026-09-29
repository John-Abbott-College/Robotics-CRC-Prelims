# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 1.
Ceci est le fichier template pour la partie 4 du Prelim 1.
"""

def part_4(positions: [(int, int, int)]):
    """
    Find the closest preys to the platypus

    Parameters:
        positions [(int, int, int)]: The position of the platypus and all the preys

    Returns:
        [int]: The ascending order of the preys' distance to the platypus
    """
    order = []
    ### You code goes here ###
    ### Votre code va ici ###

    result =[]

    for i in positions[1:]:
        platypus = positions[0]
        pos = positions.index(i) #The fish in particular
        a = (platypus[0]- i[0])**2
        b= (platypus[1]-i[1])**2
        c= (platypus[2]-i[2])**2
        
        dist = (a+b+c)**0.5 #Calculates the distance
        
        result.append([dist, pos]) #Gathers the distance of each fish 
    

   
   
   
    SortedResults = sorted(result) #Sorts the fish from closest to furthest
         
    for x in SortedResults: #Sorts the fish in the "order" list without the distances
             order.append(x[1])
          
    
    
    
    print(order)
    


    return order
