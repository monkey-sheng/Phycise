def Verify(UserInput,ValidList):
    verification=0
    for element in ValidList:
        if UserInput==element:
            verification=1
            break
    return(verification)
            
        
    
