def fixer():
    import os
    if os.path.exists("UserChoice.txt"):
        os.remove("UserChoice.txt")
    if os.path.exists("MCQnumber.txt"):
        os.remove("MCQnumber.txt")
    if os.path.exists("chosen category.txt"):
        os.remove("chosen category.txt")
    if os.path.exists("temp check.txt"):
        os.remove("temp check.txt")

