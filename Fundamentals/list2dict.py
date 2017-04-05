def l2d(list1, list2):
    return dict(zip(list1, list2))

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# print l2d(name, favorite_animal)

def altL2D(list1, list2):
    new_dict = {}
    for i in range(len(list1)):
        new_dict[list1[i]] = list2[i]
    return new_dict
print altL2D(name, favorite_animal)
