###### Controls Here!
mode = "Debug" #Modes: Debug, Watch
compactVisulaization = False
state = "M>" #Starting state of the matchine

#? [cell] [State] [New Cell] [New State] [Direction (>, <, -)]
#! seperate all inputs with spaces
string = '''# put the machine instructions here
_ M> _ M> >
Xor M> Xor Xor> >
1 Xor> 1 1 >
0 Xor> 0 0 >
1 1 1 N >
1 0 1 Y >
0 0 0 N >
0 1 0 Y >
_ Y Y M> >
_ N N M> >
E ? E E E
#'''

inputString = "_ _ _ _ _ Xor 1 1 _ E" 
#The starting state of the machine

######! End Controls

strip = {0 : "_"}
index = 0
lowestValue = 0
lastUsedRule = -1
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
    global lastUsedRule
    for i in range(len(rules)):
        if rules[i][0] == getHeadValue() and rules[i][1] == "?":
            lastUsedRule = i
            return i
        if rules[i][0] == "?" and rules[i][1] == state:
            lastUsedRule = i
            return i
        if rules[i][0] == getHeadValue() and rules[i][1] == state:
            lastUsedRule = i
            return i
    print("Rule error")
    printData()
    raise Exception(f"no rule: Head: {getHeadValue()} : State: {state}")

def run():
    global strip
    global state
    value = checkRules()
    strip[index] = rules[value][2]
    state = rules[value][3]
    if rules[value][4] == "E":
        print("End")
        printData()
        exit()
    moveHead(rules[value][4])

def printData():
    newList = []
    for i in range(len(strip)):
        if i == index:
            newList.append(f"[{strip[lowestValue + i]}]")
        else:
            if compactVisulaization == False:
                newList.append(f" {strip[lowestValue + i]} ")
            else:
                newList.append(f" {strip[lowestValue + i]} ")
    if mode == "Debug":
        print(f"Tape: {newList} | LV: {lowestValue} | State: {state} | LSR: {lastUsedRule + 1}")
    elif mode == "Watch":
        print(newList)

def Inputs():
    splitInputs = inputString.split(" ")
    global strip
    if len(splitInputs) < 0:
        return
    if len(splitInputs) == 1:
        strip[0] = splitInputs[0]
        return
    strip[0] = splitInputs[0]
    splitInputs.pop(0)
    for i in range(len(splitInputs)):
        strip.update({i + 1 : splitInputs[i]})

Inputs()
parseRuleString(string)
for i in range(100000):
    printData()
    run()
print("Time out")
printData()
