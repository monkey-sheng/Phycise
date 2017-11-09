def LaunchQuiz():
    import generate_random
    import read_all_category
    import search_number_by_category
    MCQFile=open("MCQnumber.txt","w")
    MCQFile.close()
    ChosenCategoryFile=open("chosen category.txt","w")
    ChosenCategoryFile.close()
    RandomlyChosenCategoryList=[]
    AllCategoryList=read_all_category.ReadAllCategory()
    RandomlyChosenCategoryList=generate_random.GenerateFromList(AllCategoryList,5)
    ChosenCategoryFile=open("chosen category.txt","a")
    for category in RandomlyChosenCategoryList:
        ChosenCategoryFile.write(category+"\n")
    ChosenCategoryFile.close()
    #produce five categories of MCQ
    for EachCategory in RandomlyChosenCategoryList:
        EachCategoryList=search_number_by_category.SearchNumberByCategory(EachCategory)
        #choose 3 MCQs
        RandomlyChosenNumber=generate_random.GenerateFromList(EachCategoryList,3)
        MCQfile=open("MCQnumber.txt","a")
        for EachNumber in RandomlyChosenNumber:
            MCQfile.write(EachNumber+"\n")
        MCQfile.close()
    UserChoiceFile=open("UserChoice.txt","w")
    UserChoiceFile.close()
    return("end launch_quiz")
#GenerateFromList should be alright when every category has >=3 MCQs
#somewhere in the end MCQfile.txt should be removed!!!!


#launch quiz should do no more than initializing the whole quiz
#it should return a list of the numbers of all the questions that will be printed out for the user

    
    
