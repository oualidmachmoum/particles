
def init():
    """This function will define initial configuration of the chamber 
    and particles speed, from user's inputs"""
    
    #Boolean to check if inital config respects constraint( R L .)
    initOk = False
    
    #Boolean to check if speed respects constaint (0<speed<10)
    speedOk = False

    
    #While loop for init input and constraint check
    while (initOk == False):
        print("Could you enter initial config, please respect location configs ( . L R ) :")
        init = input() #Initial configuration of the chamber 
        initOk=True
        for c in init : 
            if (c == 'R' or c == 'L' or c == '.'):
                continue
            else:
                initOk=False
                print("Error : Wrong format")
                break;

    #While loop for speed input and constraint check
    while (speedOk == False):
        print("Could you enter particle's speed,please respect (0<speed<11) :")
        speed = input() #Number of positions each particle moves in one time unit
        speedInt = int(speed) #convert speed_input to int, to check constraint
        if(1>speedInt or speedInt >10): #check constraint 0<speed<10
            print("wrong speed format")
        else:
           speedOk = True #speed input format is ok
     
                
    #return initial config list and speed
    return(speed,init)
