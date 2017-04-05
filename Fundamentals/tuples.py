my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def toTupleList(my_dict):
    return my_dict.items()



def altTupleList(my_dict):
    
    list1 = []
    for key in my_dict:
        list1.append((key, my_dict[key]))
    return list1
print altTupleList(my_dict)

