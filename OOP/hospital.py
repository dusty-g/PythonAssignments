# need to add function to check which beds are available and assign accordingly

import random
class Patient(object):
    def __init__(self, name, allergies):
        self.id = random.randint(1000, 9999)
        self.name = name
        self.allergies = allergies
        self.bed = None
class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.beds = []
        self.bedCount = 0
        
    def admit(self, patient1):
        if len(self.beds) >= self.capacity:
            print "Sorry, we're full"
        else:
            patient1.bed = self.bedCount
            self.beds.append(patient1)
            self.bedCount +=1
        return self
    def discharge(self, id1):
        for i, val in enumerate(self.beds):
            if val.id == id1:
                print "get outta here", val.name
                val.bed = None
                self.beds.pop(i)
                self.bedCount -= 1
                
                return self
        print "they're not here"
        return self




        







bob = Patient("Bob", ["bees", "peanuts"])
jane = Patient("Jane", ["dogs"])
bill = Patient("Bill", [])
hospital1 = Hospital("hospital", 5)
hospital1.admit(jane).admit(bill).admit(bob)
hospital1.discharge(bill.id).discharge(bob.id)


