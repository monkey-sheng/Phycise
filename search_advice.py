def SearchAdvice(TypeOfAdvice):#returns the content of advice
    import re
    file=open("advice file.txt","r")
    AllAdvice=file.read()
    sign="#"+str(TypeOfAdvice)+"#"
    raw_p=sign+".+"+sign
    pattern=re.compile(raw_p,re.S)
    RawContent=pattern.findall(AllAdvice)
    file.close()
    RawContentString=str(RawContent[0])
    SignLength=len(sign)
    AdviceString=""
    for char in range(SignLength,len(RawContentString)-SignLength):
        AdviceString+=RawContentString[char]
    return(AdviceString)
