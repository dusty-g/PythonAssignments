import random

def tossCoins(tosses):
    print "Starting..."
    headsTotal = 0
    tailsTotal = 0
    for i in range(tosses+1):
        string1 = "Attempt #" + str(i)
        toss = round(random.random())
        if toss == 1:
            headsTotal += 1
            string1 += "....It's heads!..."
            
        else:
            tailsTotal += 1
            string1 += "....It's tails!..."
        string1 += str(headsTotal)+ " heads and " + str(tailsTotal) + " tails so far"
        print string1
tossCoins(5000)