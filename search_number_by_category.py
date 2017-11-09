def SearchNumberByCategory(CategoryChosen):#returns a list of number of questions specified
    import re
    file=open(r"categories.txt")
    key=file.read()
    raw_p=r".+"+CategoryChosen
    pattern=re.compile(raw_p)
    ContentList=pattern.findall(key)
    file.close()
    RawQuestionList=[]
    for i in ContentList:
        c_pattern=r"\d\d*"
        pattern=re.compile(c_pattern)
        RawQuestionList=RawQuestionList+pattern.findall(i)
    QuestionNumberList=[]
    for q in RawQuestionList:
        QuestionNumberList=QuestionNumberList+[q]
    return(QuestionNumberList)
