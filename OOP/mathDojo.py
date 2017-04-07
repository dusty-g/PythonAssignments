class MathDojo(object):
    def __init__(self):
        self.start = 0
    def add(self, *numbers):
        total = 0
        for i in numbers:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    total += j
            else:
                total += i
        self.start += total
        return self
    def subtract(self, *numbers):
        total = 0
        for i in numbers:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    total += j
            else:
                total += i
        self.start -= total
        return self
    def result(self):
        return self.start
md = MathDojo()
md.add((1,2),3, [4,5])
print md.result()
md.subtract((1,2),4,[4,5])
print md.result()
