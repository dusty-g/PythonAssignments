def multiply(list1, a):
    for i in range(len(list1)):
        list1[i] *= a
    return list1
print(multiply([2,4,10,16], 5))