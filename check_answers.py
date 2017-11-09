def CheckAnswers():#erase check_file in the end
    import search_category_by_number
    import re
    UserChoice=open("UserChoice.txt","r")
    pattern=re.compile("\w+")
    AllChoicesList=pattern.findall(UserChoice.read())
    UserChoice.close()
    answers=open("answers.txt","r")
    AnswerFile=answers.read()
    answers.close()
    check_file=open("temp check.txt","w")
    check_file.close()

    for EachChoice in AllChoicesList:
        NumPattern=re.compile("\d+")
        QuestionNumberL=NumPattern.findall(EachChoice)
        QuestionNumber=QuestionNumberL[0]
        ChoicePattern=re.compile("[ABCD]")
        ChoiceMadeL=ChoicePattern.findall(EachChoice)
        ChoiceMade=ChoiceMadeL[0]
        if ChoiceMade!=AnswerFile[int(QuestionNumber)-1]:
            category=search_category_by_number.SearchCategoryByNumber(QuestionNumber)
            check_file=open("temp check.txt","a")
            check_file.write(category+"\n")
            check_file.close()
    return("end check_answers")
            
            
            
        
