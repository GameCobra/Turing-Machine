###### Controls Here!
state = "M>" #Starting state of the matchine

#? [cell] [State] [New Cell] [New State] [Direction (>, <, -)]
#? seperate all inputs with spaces
string = '''# put the machine instructions here
#Move if blank spaces
_ M> _ M> >
#When it encounters numbers
0 M> 0 A0 >
1 M> 1 A1 >
#Second round of numbers
0 A0 0 B0 >
0 A1 0 B1 >
1 A0 1 B1 >
1 A1 1 B2 >
#Therd set of numbers
0 B0 0 C0 >
1 B0 1 C1 >
0 B1 0 C1 >
1 B1 1 C2 >
0 B2 0 C2 >
1 B2 1 C3 >
#Writing the result 1
_ C0 0 D0 >
_ C1 1 D0 >
_ C2 0 D1 >
_ C3 1 D1 >
#Writing the result 2
_ D0 0 M> >
_ D1 1 M> >
E ? E E E
#'''

inputString = "_ 1 0 1 _ _ _ _ E" 
#The starting state of the machine

######! End Controls / start Mode
mode = "Debug" #Modes: Debug, Watch
compactVisulaization = False
######! End Mode




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
