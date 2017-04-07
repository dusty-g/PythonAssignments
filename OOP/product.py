class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        return self.price * (1 + tax)
    def returnItem(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "new":
            self.status = "for sale"
            return self
        elif reason == "opened":
            self.price = self.price * .80
            self.status = "used"
            return self
        else:
            print "NO RETURNS!"
            return self
    def displayInfo(self):
        print "Price: $ ", self.price
        print "name: ", self.name
        print "weight: ", self.weight
        print "brand: ", self.brand
        print "cost: $", self.cost
        print "Status: ", self.status
        return self
coke = Product(1, "Coke (bottle)", "20oz", "Coca-Cola", .50)
gum = Product(.50, "Chewing Gum", "1oz", "Juicy Fruit", .25)
# coke.displayInfo()
# coke.returnItem("I wanted a pepsi")
# coke.sell()
print str(coke.name)