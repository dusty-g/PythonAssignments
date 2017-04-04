def multiTable(size):
    line = "x"
    multiList = []
    for i in range(size):
        line += " "+str(i + 1)
        multiList.append(i + 1)
    print line

    for i in range(size):
        line = str(i + 1)
        for j in range (size):
            line += "  "+ str((j + 1) * (i + 1))
        print line
    


multiTable(9)
