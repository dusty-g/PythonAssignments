def draw_stars(x):
    for i in x:
        line = ""
        for j in range(i):
            line += "*"
        print line


def drawStrings(list1):
    for i in list1:
        if isinstance(i, int):
            line = ""
            for j in range(i):
                line += "*"
            print line
        else:
            line = ""
            for j in i:
                line += i[0]
            print line
drawStrings([4, 6, 1, 3,"5...", "dog", "cat"])