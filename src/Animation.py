

def animation(speed,init):
    '''Function for the animation of the process'''
   
    lenght = len(init) #number of locations in the chamber
    
    chamberState=[""]*lenght #Define list for the Chamber's State with occupied and unoccupied locations 
    #Loop to Initialize Chamber's State with occupied and unoccupied locations
    for i in range(lenght):
        if(init[i]=="L" or init[i]=="R"):
            chamberState[i]="X"
        else:
            chamberState[i]="."
    #Display of the Initial chamber's state
    print('{')
    affiche_to_str(chamberState)
    
    
    speed=int(speed)#the number of positions each particle moves in one time unit
    timeUnit=1 #Elapsed time units
    totalDistance = timeUnit*speed #Total Distance travelled by a particle (from Initial Config)
    finalChamberState=["."]*lenght#Final chamber state {......}
    
    
    
    #Processing loop
    while (chamberState != finalChamberState):  # While chamber didn't reach final state, processing loop continues 
        print(',')
        
        #If speed >= chamber_lenght, the next state of the chamber will be the final state
        if (totalDistance>=lenght):
            chamberState = finalChamberState
            affiche_to_str(chamberState)
        #Else, go checking particles caracteristics
        else :
            for i in range (lenght): #Loop to Browse Through ChamberConfig
                
                #Most Critical case, Positions no longer reachable by a particle, regarding Distance Travelled
                if (i>=lenght-totalDistance and i <totalDistance):
                    chamberState[i]="."
                
                #Critical case, Position only reachable by Leftward particles
                elif(i<totalDistance):
                    if(init[i+totalDistance]=="L"):
                        chamberState[i] = "X"
                    else:
                        chamberState[i]="."
                
                #Critical case, Position only reachable by Rightward particles
                elif(i>=lenght-totalDistance):
                    if(init[i-totalDistance]=="R"):
                        chamberState[i]="X"
                    else:
                        chamberState[i]="."
                        
                #Casual case, Positions possibly reachable by Rightward or Leftward particles
                else:
                    if(init[i+totalDistance]=="L" or init[i-totalDistance]=="R"):
                        chamberState[i]="X"
                    else:
                        chamberState[i]="."
           
            #Display chamber'state with occupied and unoccupied locations, after processing
            affiche_to_str(chamberState)
            
            timeUnit=timeUnit+1 #increment time 
            totalDistance=timeUnit*speed #Ubdate Total Distance travelled by particle
    print("}")


def affiche_to_str(liste):
    '''function to display chamberState'''
    print('"',end="")
    str1 = ''.join(liste)
    print(str1,end="")
    print('"',end="")
