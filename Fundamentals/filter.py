def filterByType(value):
    if isinstance(value, int):
        if value >= 100:
            print "That's a big number"
        else:
            print "That's a small number"
    elif isinstance(value, str):
        if len(value) >= 50:
            print "Long sentance."
        else:
            print "Short sentance."
    elif isinstance(value, list):
        if len(value) >= 10:
            print "Big list!"
        else:
            print "Short list."