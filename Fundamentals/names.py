students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# iterate through the objects in the array
for objects in students:
    # iterate through the keys in the objects
    line = ""
    for key in objects:
        line += objects[key] + " "
    print line

