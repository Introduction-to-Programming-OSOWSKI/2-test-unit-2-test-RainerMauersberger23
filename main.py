def isDozen(d):
    if d % 2 == 0:
        return True
    else:
        return False

print(isDozen(12))




def waterState(state):
    
    if state == "20":
        return "solid"

    elif state == "10":
        return "liquid"

    else:
        return "gas"

print(waterState(20))


def stopLight(color):
    if color == "green":
        return "Go"
    elif color == "yellow":
        return "Slow"
    
    else:
        return "Stop"

print(stopLight("green"))

