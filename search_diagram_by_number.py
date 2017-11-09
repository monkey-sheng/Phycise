def SearchDiagramByNumber(QuestionNumber):#returns the diagram path
    import re
    import os
    abspath=str(os.path.abspath('.'))
    path=abspath+r"\question with diagram.txt"
    file=open(path)
    key=file.read()
    sign=QuestionNumber
    pattern=re.compile("\d+")
    ContentList=pattern.findall(key)
    file.close()
    if QuestionNumber not in ContentList:
        result=0
    else:
        result=abspath+"\diagrams\\"+str(QuestionNumber)+".jpg"
        
    
    return(result)  

