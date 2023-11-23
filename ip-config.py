global cl
cl = ''

def integrateIP(a, b, c, d):
    out = 0
    out += a
    aout = out << 8
    aout += b
    bout = aout << 8
    bout += c
    cout = bout << 8
    cout += d 
    return format(cout, '032b')

def printIP(ip):
    ip = str(ip)
    for i in range(32):
        print(ip[i], end="") #this syntax makes it so it doesn't go to the next line
        if (i == 7) or (i == 15) or (i == 23):
            print(".", end="")
    print()

def printSM(ipHasClass):
    asm = 0
    if ipHasClass:
        clCheck = int(octets[0])
    if clCheck < 127:
        cl = 'A'
        asm += 255
        sm = asm << 24
    elif clCheck < 192:
        cl = 'B'
        asm += 255
        bsm = asm << 8
        bsm += 255
        sm = bsm << 16
    elif clCheck < 224:
        cl = 'C'
        asm += 255
        bsm = asm << 8
        bsm += 255
        csm = bsm << 8
        csm += 255
        sm = csm << 8
    return format(sm, '032b')
    
def printDG():
    dg = int(ipv4, 2) & int(sm, 2)
    return format(dg, '032b')

def printFA():
    fa = int(dg, 2) + 1
    return format(fa,'032b')

def printBA():
    res = 0
    if int(octets[0]) < 127: #if class is A
        ares = int(octets[0])
        bres = ares << 8
        bres += 255
        cres = bres << 8
        cres += 255
        res = cres << 8 
        res += 255
    elif int(octets[0]) < 192: #if class is B
        res = int(octets[0])
        res = res << 8
        res += int(octets[1])
        res = res << 8
        res += 255
        res = res << 8 
        res += 255
        res = res << 8
        res += 255
    elif int(octets[0]) < 224: #if class is C
        ares = int(octets[0])
        bres = ares << 8
        bres += int(octets[1])
        cres = bres << 8
        cres += int(octets[2])
        res = cres << 8 
        res += 255
    return format(res, '032b')

def printLA():
    la = int(ba, 2)
    la -= 1
    return format(la,'032b')

input = input("Please enter IP: ")
octets = input.split('.')

ipv4 = integrateIP(int(octets[0]),int(octets[1]), int(octets[2]), int(octets[3]))
print("IP: ", end="")
printIP(ipv4)

sm = printSM(1)
print("SM: ", end="")
printIP(sm)

dg = printDG()
print("DG: ", end="")
printIP(dg)

fa = printFA()
print("FA: ", end="")
printIP(fa)

ba = printBA()
print("BA: ", end="")
printIP(ba)

la = printLA()
print("LA: ", end="")
printIP(la)