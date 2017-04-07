class Call(object):
    def __init__(self, name, number, time, reason):
        self.id = "#" + str(number)
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def displayInfo(self):
        print self.id
        print self.name
        print self.number
        print self.time
        print self.reason
    
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
    def addCall(self, call):
        self.calls.append(call)
        self.queue = len(self.calls)
        return self
    def removeCall(self):
        self.calls.pop(0)
        self.queue = len(self.calls)
        return self
    def queueInfo(self):
        print "queue length is", self.queue
        for i in self.calls:
            print i.name, i.number
        return self
    def removeNumber(self, number):
        
        for i, val in enumerate(self.calls):
            if val.number == number:
                self.calls.pop(i)
        self.queue = len(self.calls)
        return self
        
call1 = Call("bob", 4443234, "3:30", "Needs help")
call2 = Call("jane", 4452314, "3:40", "complaint")
call3 = Call("joe", 5551963, "3:42", "none")
center = CallCenter()
center.addCall(call1).addCall(call2).queueInfo()
center.removeNumber(4443234).queueInfo()
center.addCall(call3).queueInfo()