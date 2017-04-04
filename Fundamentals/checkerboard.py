def checker(rows, columns):
    
    for i in range (rows):
        totalRow = ""
        for j in range(columns):
            if i %2 == 0:
                totalRow += "* "
            else:
                totalRow += " *"
        print totalRow