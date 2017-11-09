def ProduceAdvice():
    import re
    file=open("temp check.txt","r")
    MistakesFile=file.read()
    pattern=re.compile("\w.+")
    MistakesList=pattern.findall(MistakesFile)
    file.close()
    RandomlyChosenCategory=open("chosen category.txt","r")
    RandomlyChosenCategoryFile=RandomlyChosenCategory.read()
    pattern=re.compile("\w.+")
    RandomlyChosenCategoryList=pattern.findall(RandomlyChosenCategoryFile)
    MistakesMadeTimes=[]
    for ChosenCategory in RandomlyChosenCategoryList:
        count=MistakesList.count(ChosenCategory)
        MistakesMadeTimes+=[count]
    AdviceFile=open("advice file.txt","r")
    AllAdvice=AdviceFile.read()
    MistakeSum=0
    for each in MistakesMadeTimes:
        MistakeSum+=each
    if MistakeSum==0:
        TypeOfAdvice="GeneralLevel6"
        import search_advice
        advice=search_advice.SearchAdvice(TypeOfAdvice)
        print(advice)
    if MistakeSum==1:
        TypeOfAdvice="GeneralLevel5"
        import search_advice
        advice=search_advice.SearchAdvice(TypeOfAdvice)
        print(advice)
    if 2<=MistakeSum<=3:
        TypeOfAdvice="GeneralLevel4"
        import search_advice
        advice=search_advice.SearchAdvice(TypeOfAdvice)
        print(advice)
    if 4<=MistakeSum<=6:
        TypeOfAdvice="GeneralLevel3"
        import search_advice
        advice=search_advice.SearchAdvice(TypeOfAdvice)
        print(advice)
    if 7<=MistakeSum<=10:
        TypeOfAdvice="GeneralLevel2"
        import search_advice
        advice=search_advice.SearchAdvice(TypeOfAdvice)
        print(advice)
    if 11<=MistakeSum<=14:
        TypeOfAdvice="GeneralLevel1"
        import search_advice
        advice=search_advice.SearchAdvice(TypeOfAdvice)
        print(advice)
    if MistakeSum==15:
        print("Come on! This is a quiz!\nYou are either too unlucky to get everything wrong,\nor you actually knows the correct answer and did this on purpose.")
    GoodTopic=[]    
    for j in range(0,len(MistakesMadeTimes)-1):
        if MistakesMadeTimes[j]==0:
            GoodTopic+=RandomlyChosenCategoryList[j]
    if len(GoodTopic)==1:
        advice="Seems that your only good topic is "
        print(advice+GoodTopic[0]+", keep up the good work!")
    elif len(GoodTopic)>1:
        for k in range(0,len(GoodTopic)-1):
            advice="Seems that your good topics are "
            if k!=len(GoodTopic)-1 and k!=0:
                GoodTopic[k]=", "+GoodTopic[k]
            if k==len(GoodTopic)-1:
                GoodTopic[k]=" and "+GoodTopic[k]
        AdviceString=""
        for p in range(0,len(GoodTopic)-1):
            AdviceString+=str(GoodTopic[p])
            
        advice=advice+AdviceString
        print(advice)
    AdviceString=""
    for v in range(0,len(MistakesMadeTimes)-1):
        if MistakesMadeTimes[v]>=2:
            TypeOfAdvice=RandomlyChosenCategoryList[v]
            advice=search_advice.SearchAdvice(TypeOfAdvice)
            AdviceString+=advice
    print(AdviceString)
    return("end produce_advice") 







        
