strip = {0 : "_"}
index = 0

def moveHead(amount : int):
    global index
    index += amount
    try:
        strip[index]
    except:
        strip.update({index : "_"})

for i in range(10):
    moveHead(-1)

print(strip)
