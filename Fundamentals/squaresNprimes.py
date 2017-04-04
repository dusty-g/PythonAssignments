
def squares(end):

    count = 1
    maxSquare = 0
    squaresList = []
    while maxSquare < end:
        squaresList.append(count * count)
        maxSquare = count * count
        count += 1
    return squaresList

def isPrime(x):
    for i in range(x//2):
        if x % (i+2) == 0:
            return False
    
    return True

def fooBar(beginning, end):
    squaresList = squares(end)
    print squaresList
    for i in range(beginning, end+1):
        
        
        if i in squaresList:
            
            print str(i)+ " is square"
        if isPrime(i):
            print str(i) + " is prime"
fooBar(100, 10000)