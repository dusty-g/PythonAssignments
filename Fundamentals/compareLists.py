def compare(list1, list2):
    if len(list1) != len(list2):
        print "The lists are not the same"
    else:
        for i in range(len(list1)):
            if list1[i] == list2[i]:
                continue
            else:
                print "The lists are not the same"
                break
            print "The lists are the same"