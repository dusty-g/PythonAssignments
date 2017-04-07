class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print self.name, self.health

# bird = Animal("dave")
# bird.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    
    def __init__(self, name):
        super(Dog, self).__init__(name) 
        self.health = 140
    def bark(self):
        print "woof"
    def pet(self):
        self.health += 5

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "dragon!"
        super(Dragon, self).displayHealth()

sparky = Dog("spot")
sparky.bark()
sparky.run()
sparky.displayHealth()

puff = Dragon("Puff")
puff.fly()
puff.displayHealth()
