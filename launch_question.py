def LaunchQuestion(lang):
    import re
    import search_content_by_number
    import search_diagram_by_number
    import verify_valid_input
    import print_diagram
    file=open("MCQnumber.txt","r")
    content=file.read()
    pattern=re.compile("\d+")
    QuestionNumberList=pattern.findall(content)
    file.close()
    UserChoiceFile=open("UserChoice.txt","a")
    i=0
    while i<=len(QuestionNumberList)-1:
        content=search_content_by_number.SearchContentByNumber(QuestionNumberList[i])
        print(content)
        #check and print diagam below
        diagram=search_diagram_by_number.SearchDiagramByNumber(QuestionNumberList[i])
        if diagram!=0:
            print_diagram.PrintDiagram(diagram)
        if lang=="1":
            UserChoice=input("Your choice is：")
        if lang=="2":
            UserChoice=input("你的选择是: ")
        VerifyResult=verify_valid_input.Verify(UserChoice,['A','B','C','D'])
        if VerifyResult==1:
            UserChoiceFile.write(str(QuestionNumberList[i])+UserChoice+"\n")
            i=i+1
            if i<len(QuestionNumberList):
                if lang=="1":
                    print("Next Question:\n")
                elif lang=="2":
                    print("下一题")
        else:
            if lang=="1":
                print("Please input Uppercase A,B,C or D only.\nTry again\n")
            elif lang=="2":
                print("请输入大写的ABCD\n再试一次\n")
    UserChoiceFile.close()
    if lang=="1":
        print("You have done all the MCQs! Let's take a look at how well you have done.\n\n")
    elif lang=="2":
        print("你完成了所有的选择题！ 来看看你做得如何吧\n\n")
    import time
    time.sleep(2)
    return("end launch_question")
