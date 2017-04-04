def findAndReplace(string):
    print string.find("day")
    print string.replace("day", "month")
findAndReplace("It's thanksgiving day. It's my birthday,too!")

def minMax(list1):
    tempMax = list1[0]
    tempMin = list1[0]
    for i in list1:
        if i > tempMax:
            tempMax = i
        if i < tempMin:
            tempMin = i
    print "max = ", tempMax, "min = ", tempMin
minMax([2,54,-2,7,12,98])

def firstLast(list1):
    print list1[0]
    print list1[-1]
    newList = [list1[0], list1[-1]]
    print newList
firstLast(["hello",2,54,-2,7,12,98,"world"])

def makeNewList(list1):
    newList1=[]
    newList1.append(sorted(list1)[: len(list1)//2])
    for i in sorted(list1)[len(list1)//2:]:
        newList1.append(i)
    print newList1
makeNewList([19,2,54,-2,7,12,98,32,10,-3,6])





