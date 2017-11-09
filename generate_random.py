def GenerateRandint(number):#could have duplicates
    import random
    return(random.randint(0,number))
        
def GenerateFromList(List,n):#doesn't have duplicates
    import random
    return(random.sample(List,n))
