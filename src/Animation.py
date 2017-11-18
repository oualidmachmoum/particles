

def animation(speed,init):
    '''Function for the animation of the process'''
   
    lenght = len(init) #number of locations in the chamber
    
    chamberState=[""]*lenght #Define list for the Chamber's State with occupied and unoccupied locations 
    #Loop to Initialise Chamber's State with occupied and unoccupied locations
    for i in range(lenght):
        if(init[i]=="L" or init[i]=="R"):
            chamberState[i]="X"
        else:
            chamberState[i]="."
    #Display of the Initial chamber's state
    print('{')
    affiche_to_str(chamberState)
    
    
    speed=int(speed)#the number of positions each particle moves in one time unit
    stateNumber=1 #Numero of chamber's state
    totalMovAmp = stateNumber*speed #Total Amplitude of particule movement (from Initial Config)
    finalChamberState=["."]*lenght#Final chamber state {......}
    
    
    
    #Processing loop
    while (chamberState != finalChamberState):  # While chamber didn't reach final state, processing loop continues 
        print(',')
        
        #If speed >= chamber_lenght, the next state of the chamber will be the final state
        if (totalMovAmp>=lenght):
            chamberState = finalChamberState
            str1 = ''.join(chamberState)
            print(str1)
            return "terminé"
        #Else, go checking particules caracteristics
        else :
            for i in range (lenght): #Loop to Browse Through ChamberConfig
                
                #Most Critical case, Positions no longer reachable by a particule, regarding TotalMovAmplitude
                if (i>=lenght-totalMovAmp and i <totalMovAmp):
                    chamberState[i]="."
                
                #Critical case, Position only reachable by Leftward particules
                elif(i<totalMovAmp):
                    if(init[i+totalMovAmp]=="L"):
                        chamberState[i] = "X"
                    else:
                        chamberState[i]="."
                
                #Critical case, Position only reachable by Rightward particules
                elif(i>=lenght-totalMovAmp):
                    if(init[i-totalMovAmp]=="R"):
                        chamberState[i]="X"
                    else:
                        chamberState[i]="."
                        
                #Casual case, Positions possibly reachable by Rightward or Leftward particules
                else:
                    if(init[i+totalMovAmp]=="L" or init[i-totalMovAmp]=="R"):
                        chamberState[i]="X"
                    else:
                        chamberState[i]="."
           
            #Display chamber'state with occupied and unoccupied locations, after processing
            affiche_to_str(chamberState)
            
            stateNumber=stateNumber+1 #Increment stateNumber, chamber has just known one more time-unit processing
            totalMovAmp=stateNumber*speed #Ubdate Total amplitude of Particule Movement (since initial config)
    print("}")


def affiche_to_str(liste):
    print('"',end="")
    str1 = ''.join(liste)
    print(str1,end="")
    print('"',end="")
