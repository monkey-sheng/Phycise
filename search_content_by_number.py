def SearchContentByNumber(QuestionNumber):#returns the question content
    import re
    path=r"all questions.txt"
    file=open(path)
    key=file.read()
    sign="#"+str(QuestionNumber)+"#"
    raw_p=sign+r".+"+sign
    pattern=re.compile(raw_p,re.S)
    RawContent=pattern.findall(key)
    file.close()
    RawContentString=str(RawContent[0])
    SignLength=len(sign)
    ContentString=""
    for char in range(SignLength,len(RawContentString)-SignLength):
        ContentString+=RawContentString[char]
    return(ContentString)
