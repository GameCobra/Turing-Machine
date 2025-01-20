###### Controls Here!
state = "SS" #Starting state of the matchine

#? [cell] [State] [New Cell] [New State] [Direction (>, <, -)]
#? seperate all inputs with spaces
string = '''# put the machine instructions here
#* Offset start by 1 cell
P SS P S >
#* Add space to the next cell
0 S 0 G >
1 S 1 G >
0 G N g0 >
1 G N g1 >
#* Shift everything over
0 g0 0 g0 >
0 g1 1 g0 >
1 g0 0 g1 >
1 g1 1 g1 >
#* return
_ g0 0 <R <
_ g1 1 <R <
0 <R 0 <R <
1 <R 1 <R <
N <R N S >
#* Return 2
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
#* Return to end
P <R2 P R3> >
0 R3> 0 R3> >
1 R3> 1 R3> >
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
P <R4 P S>1 >
#* Move over
? S>1 ? R32> >
#* Rearange
? R32> ? R31 >
? R31> ? R30> >
? R30> ? R29> >
? R29> ? R28> >
? R28> ? R27> >
? R27> ? R26> >
? R26> ? R25> >
? R25> ? R24> >
? R24> ? R23> >
? R23> ? R22> >
? R22> ? R21> >
? R21> ? R20> >
? R20> ? R19> >
? R19> ? R18> >
? R18> ? R17> >
? R17> ? R16> >
? R16> ? R15> >
? R15> ? R14> >
? R14> ? R13> >
? R13> ? R12> >
? R12> ? R11> >
? R11> ? R10> >
? R10> ? R9> >
? R9> ? R8> >
? R8> ? R7> >
? R7> ? R6> >
? R6> ? R5> >
? R5> ? R4> >
? R4> ? R3> >
? R3> ? R2> >
? R2> ? R1> >
#* 0 Back
0 R1> NNN <32R0 >
? <32R0 ? <31R0 <
? <31R0 ? <30R0 <
? <30R0 ? <29R0 <
? <29R0 ? <28R0 <
? <28R0 ? <27R0 <
? <27R0 ? <26R0 <
? <26R0 ? <25R0 <
? <25R0 ? <24R0 <
? <24R0 ? <23R0 <
? <23R0 ? <22R0 <
? <22R0 ? <21R0 <
? <21R0 ? <20R0 <
? <20R0 ? <19R0 <
? <19R0 ? <18R0 <
? <18R0 ? <17R0 <
? <17R0 ? <16R0 <
? <16R0 ? <15R0 <
? <15R0 ? <14R0 <
? <14R0 ? <13R0 <
? <13R0 ? <12R0 <
? <12R0 ? <11R0 <
? <11R0 ? <10R0 <
? <10R0 ? <9R0 <
? <9R0 ? <8R0 <
? <8R0 ? <7R0 <
? <7R0 ? <6R0 <
? <6R0 ? <5R0 <
? <5R0 ? <4R0 <
? <4R0 ? <3R0 <
? <3R0 ? <2R0 <
? <2R0 ? <1R0 <
? <1R0 0 RR>4 <
#* 1 Back
1 R1> NNN <32R1 >
? <32R1 ? <31R1 <
? <31R1 ? <30R1 <
? <30R1 ? <29R1 <
? <29R1 ? <28R1 <
? <28R1 ? <27R1 <
? <27R1 ? <26R1 <
? <26R1 ? <25R1 <
? <25R1 ? <24R1 <
? <24R1 ? <23R1 <
? <23R1 ? <22R1 <
? <22R1 ? <21R1 <
? <22R1 ? <21R1 <
? <22R1 ? <21R1 <
? <22R1 ? <21R1 <
? <21R1 ? <20R1 <
? <20R1 ? <19R1 <
? <19R1 ? <18R1 <
? <18R1 ? <17R1 <
? <17R1 ? <16R1 <
? <16R1 ? <15R1 <
? <15R1 ? <14R1 <
? <14R1 ? <13R1 <
? <13R1 ? <12R1 <
? <12R1 ? <11R1 <
? <11R1 ? <10R1 <
? <10R1 ? <9R1 <
? <9R1 ? <8R1 <
? <8R1 ? <7R1 <
? <7R1 ? <6R1 <
? <6R1 ? <5R1 <
? <5R1 ? <4R1 <
? <4R1 ? <3R1 <
? <3R1 ? <2R1 <
? <2R1 ? <1R1 <
? <1R1 0 RR>4 <
#* 4 Over
_ R1> E <32R1 -
? RR>4 ? RR>3 >
? RR>3 ? RR>2 >
? RR>2 ? R32> >
#* End
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
            try:
                if V[4] == "<":
                    V[4] = -1
                if V[4] == ">":
                    V[4] = 1
                if V[4] == "-":
                    V[4] = 0
                rules.append(V)
            except:
                raise Exception(f"Invalid Rule: {V} - {i}")
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
    if rules[value][2] != "?":    
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
