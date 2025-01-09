strip = {0 : "_"}
index = 0
state = "_"
lowestValue = 0


rules = []

def moveHead(amount : int):
    global index
    global lowestValue
    index += amount
    try:
        strip[index]
    except:
        strip.update({index : "_"})
        if index < lowestValue:
            lowestValue = index

def getHeadValue():
    return strip[index]


def parseRuleString(value : str):
    valueList = value.splitlines()
    for i in range(len(valueList)):
        if "#" in valueList[i]:
            continue
        else:
            global rules
            # value state newvalue newstate move
            V = valueList[i].split(" ")
            if V[4] == "<":
                V[4] = -1
            if V[4] == ">":
                V[4] = 1
            if V[4] == "-":
                V[4] = 0
            rules.append(V)

def checkRules():
    for i in range(len(rules)):
        if rules[i][0] == getHeadValue() and rules[i][1] == state:
            return i
    raise Exception("no rule")

def run():
    global strip
    global state
    value = checkRules()
    strip[index] = rules[value][2]
    state = rules[value][3]
    moveHead(rules[value][4])

def printStrip():
    newList = []
    for i in range(len(strip)):
        newList.append(strip[lowestValue + i])
    print(newList)

string = '''#
_ _ 1 1 >
_ 1 2 _ >
#'''

parseRuleString(string)
for i in range(10):
    run()
printStrip()
