def typeList(list1):
    newStr = ""
    newNum = 0
    hasString = 0
    hasInt = 0
    hasFloat = 0
    for i in list1:
        if isinstance(i, str):
            hasString = 1
            newStr = newStr + " " + i
        elif isinstance(i, int):
            hasInt = 1
            newNum += i 
        elif isinstance(i,float):
            hasFloat = 1
            newNum += i
    if hasFloat + hasInt + hasString > 1:
        print "The array you entered is of mixed type"
        print "String:" + newStr
        print "Number:" + str(newNum)
    else:
        if hasFloat == 1:
            print "The array you entered is of type Float"
            print "Float:" + str(newNum)
        elif hasInt == 1:
            print "The array you entered is of type Int"
            print "Int:" + str(newNum)
        elif hasString == 1:
            print "The array you entered is of type String"
            print "String:" + newStr
    
