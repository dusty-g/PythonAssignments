users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

#  iterate over object (only has two key/value pairs)

for key in users:
    print key
    count = 1
    # iterate over the array (which contains objects)
    
    for objects in users[key]:
        length = 0
        line = str(count) + " - "

        for key2 in objects:
            line += " " + objects[key2]
            for char in objects[key2]:
                length += 1
        print line +" - "+ str(length)
        count += 1