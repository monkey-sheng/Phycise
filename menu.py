def MainMenu(lang):
    verification=0
    import verify_valid_input
    while verification==0:
        if lang=="1":
            print("Take a quiz to see how well you are doing in Physics?")
            print("Sure(Y)       Not now(N)")
            choice=input("Your choice is: ")
        if lang=="2":#汉语部分
            print("来做个小测试试身手吧？")
            print("好的（Y）    算了（N）")
            choice=input("你的选择是： ")
        verification=verify_valid_input.Verify(choice,"YN")
        if verification==0 and lang=="1":
            print(r"Please enter 'Y' or 'N'")
        elif verification==0 and lang=="2":
            print("请输入Y或N")
        else:
            break
    if choice=="Y":
            return("ContinueToQuiz")
    if lang=="1" and choice=="N":
        import time
        print("What a pity.....")
        time.sleep(2)
        return("exit")
    elif lang=="2" and choice=="N":
        import time
        print("下次再会啊...")
        time.sleep(2)
        return("exit")
            
    
        
