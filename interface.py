mainloop=1
exitflag=0
import verify_valid_input
print("Welcome!\n欢迎！")
print("Choose a language please\n请选择语言")
print("1.English 2.汉语")
LangVerification=0
while LangVerification==0:
    lang=input("Your choice is: ")
    LangVerification=verify_valid_input.Verify(lang,"12")
    if LangVerification==0:
        print("please only enter '1' for English or '2' for Chinese")
        print("请输入数字1代表英文或数字2代表汉语")
        
while mainloop==1:
    import menu
    a=menu.MainMenu(lang)
    if a=="ContinueToQuiz":
        import launch_quiz
        b=launch_quiz.LaunchQuiz()
    if a=="exit":
        result="exit"
        break
    if b=="end launch_quiz":
        import launch_question
        z=launch_question.LaunchQuestion(lang)
    if z=="end launch_question":
        import check_answers
        c=check_answers.CheckAnswers()
    if c=="end check_answers":
        import produce_advice
        d=produce_advice.ProduceAdvice()
    if d=="end produce_advice":
        import fixer
        fixer.fixer()
        result=0
        while result==0:
            if lang=="1":
                print("\nYou have finished the quiz! Do you wish to exit(E) or do you want to do another one(A)?")
                i=input("Your choice is:")
            if lang=="2":
                print("你已经完成了这个小测！你希望退出（E）还是希望再做一次（A）？")
                i=input("你的选择是： ")
            import verify_valid_input
            result=verify_valid_input.Verify(i,['A','E'])
            if result==0:
                if lang=="1":
                    print("Please only enter A or E\nTry again")
                if lang=="2":
                    print("请输入A或E\n再试一次")
            if result==1:
                if i=="E":
                    mainloop=0
                    import time
                    if lang=="1":
                        print("See ya!")
                    if lang=="2":
                        print("再见！")
                    time.sleep(2)
                    break
                if i=="A":
                    mainloop=1
exit
    
