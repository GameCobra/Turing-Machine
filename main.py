###### Controls Here!
state = "SS" #Starting state of the matchine

#? [cell] [State] [New Cell] [New State] [Direction (>, <, -)]
#? seperate all inputs with spaces
string = '''# put the machine instructions here
#Offset start by 1 cell
P SS P S >
#Add space to the next cell
0 S 0 G >
1 S 1 G >
0 G N g0 >
1 G N g1 >
#Shift everything over
0 g0 0 g0 >
0 g1 1 g0 >
1 g0 0 g1 >
1 g1 1 g1 >
#return
_ g0 0 <R <
_ g1 1 <R <
0 <R 0 <R <
1 <R 1 <R <
N <R N S >
#Return 2
_ G _ <R2 <
0 <R2 0 <R2 <
1 <R2 1 <R2 <
N <R2 NN G2 >
0 G2 NN gg0 >
1 G2 NN gg1 >
0 gg0 0 gg0 >
1 gg0 0 gg1 >
0 gg1 1 gg0 >
1 gg1 1 gg1 >
NN gg0 0 ggNN >
NN gg1 1 ggNN >
0 ggNN NN gg0 >
1 ggNN NN gg1 >
NN ggNN NN ggNN >
NN <R2 NN <R2 <
_ gg0 0 <R2 <
_ gg1 1 <R2 <
#Return to end
P <R2 P R3> >
0 R3> 0 R3> >
1 R3> 0 R3> >
NN R3> NNN R3>N >
NN R3>N NN R3> >
_ R3> _ <R4 <
0 <R4 0 <R4 <
1 <R4 1 <R4 <
NNN <R4 NNN <R4 <
NN <R4 NNN GGG >
0 GGG NNN ggg0 >
1 GGG NNN ggg1 >
0 ggg0 0 ggg0 >
1 ggg0 0 ggg1 >
0 ggg1 1 ggg0 >
1 ggg1 1 ggg1 >
NNN ggg0 0 gggNNN >
NNN ggg1 1 gggNNN >
0 gggNNN NNN ggg0 >
1 gggNNN NNN ggg1 >
NNN gggNNN NNN gggNNN >
_ ggg0 0 <R4 <
_ ggg1 1 <R4 <
P <R4 E E -
#End
E ? E E E
#'''

inputString = "P 0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0" 
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
        print(f"Tape: {newList} | LV: {lowestValue} | State: {state} | LUR: {lastUsedRule + 1}")
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
