def multiples():
    for i in range(1000):
        print i + 1
# multiples()

def multiples2():
    for i in range(5, 1000001, 5):
        print i
# multiples2()

def sumList(list1):
    temp = 0
    for i in list1:
        temp += i
    # print temp
    return temp
# sumList([1, 2, 5, 10, 255, 3])
def avgList(list1):
    print sumList(list1) / float(len(list1))
avgList([1, 2, 5, 10, 255, 3])

