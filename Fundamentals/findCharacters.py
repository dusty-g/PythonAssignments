def find(list1, string1):
    newArray = []
    for i in list1:
        if string1 in i:
            newArray.append(i)
    print newArray