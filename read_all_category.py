def ReadAllCategory():
    import re
    AllCategory=open(r"all category.txt").read()
    pattern=re.compile(r"\w.+")
    return(pattern.findall(AllCategory))
