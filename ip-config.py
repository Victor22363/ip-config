def integrateIP(a, b, c, d):
    return (a << 24) + (b << 16) + (c << 8) + d

def printIP(ip):
    ip = format(ip, '032b')
    for i in range(32):
        print(ip[i], end='')
        if (i == 7) or (i == 15) or (i == 23):
            print('.', end='')
    print()

def printSM(ipHasClass, octets):
    clCheck = 0  # Initialize clCheck outside the conditional block
    if ipHasClass:
        clCheck = int(octets[0])
    if clCheck < 127:
        result = (255 << 24)
    elif clCheck < 192:
        result = (255 << 24) + (255 << 16)
    elif clCheck < 224:
        result = ((255 << 24) + (255 << 16) + (255 << 8)) << 8
    return format(result, '032b')

def printDG(ipv4, sm):
    dg = int(ipv4, 2) & int(sm, 2)
    return format(dg, '032b')

def printFA(dg):
    fa = int(dg, 2) + 1
    return format(fa, '032b')

def printBA(octets):
    if int(octets[0]) < 127:  # if class is A
        result = (int(octets[0]) << 24) + (255 << 16) + (255 << 8) + 255
    elif int(octets[0]) < 192:  # if class is B
        result = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (255 << 8) + 255
    elif int(octets[0]) < 224:  # if class is C
        result = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + 255
    return format(result, '032b')

def printLA(ba):
    la = int(ba, 2) - 1
    return format(la, '032b')

input_str = input("Please enter IP: ")
octets = input_str.split('.')

ipv4 = integrateIP(int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3]))
print("IP: ", end="")
printIP(ipv4)

sm = printSM(1, octets)
print("SM: ", end="")
printIP(int(sm, 2))

dg = printDG(format(ipv4, '032b'), sm)
print("DG: ", end="")
printIP(int(dg, 2))

fa = printFA(dg)
print("FA: ", end="")
printIP(int(fa,2))

ba = printBA(octets)
print("BA: ", end="")
printIP(int(ba,2))

la = printLA(ba)
print("LA: ", end="")
printIP(int(la,2))
