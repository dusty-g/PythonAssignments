def isOddEven(end):
    for i in range(end+1):
        string1 = "Number is: " + str(i) + ". "
        if (i+1)% 2 == 0:
            string1 += "This is an even number."
        else:
            string1+="This is an odd number."
        print string1
isOddEven(2000)