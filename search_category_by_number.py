def SearchCategoryByNumber(QuestionNumber):#returns the question category
    import re
    file=open("categories.txt")
    key=file.read()
    sign="#"+str(QuestionNumber)+"#"
    pattern=sign+r".+"+sign
    pattern=re.compile(pattern)
    RawContent=pattern.findall(key)
    file.close()
    RawContentString=str(RawContent[0])
    SignLength=len(sign)
    category=""
    for char in range(SignLength,len(RawContentString)-SignLength):
        category+=RawContentString[char]
    return(category)

