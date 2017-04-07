class Bike(object):
    def __init__(self, price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        
    def displayInfo(self):
        print "Price is:", self.price
        print "Max Speed is", self.max_speed
        print "Miles:", self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self
bike1 = Bike(200, "15 mph")
bike2 = Bike(150, "10 mph")
bike3 = Bike(10, "1 mph")

bike1.ride().ride().ride().displayInfo()

bike3.reverse().reverse().displayInfo()
