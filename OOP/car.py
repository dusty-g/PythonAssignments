class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()
    def display_all(self):
        print "Price: $", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

fancyCar = Car(80000, "150 mph", "90%", 100)
cheapCar = Car(2000, "50 mph", "Empty", 200000)
raceCar = Car(200000, "300 mph", "Full", 500)
