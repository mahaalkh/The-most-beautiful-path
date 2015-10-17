import math

## to calculate distance
def pythg((lat1,lon1),(lat2,lon2)):
    ##1 lat = 111080.25m
    ##1 long = 82382.11m
    return math.sqrt(((lat1-lat2)*111080.25)**2 + ((lon1-lon2)*82382.11)**2)

## to convert from html to dictionary of dictionaries
def getGraph():
    src = input('Enter "file (example: "src.txt")": ')
    f = open(src,"r")
    N = {}
    AL = {}
    SN = {}
    i = 1
    inWay = False
    ii = 1
    prevnd = ''
    names = []
    for line in f:
        if line.strip().startswith("<node"):
            i += 1
            s = line.split("=")
            nid = str(s[1].split('"')[1])
            lat = float(s[8].split('"')[1])
            lon = float(s[9].split('"')[1])
            N[nid] = (lat,lon)
            AL[nid] = {}
            SN[nid] = {}
        elif line.strip().startswith("<way"):
            inWay = True
            ii += 1
        elif line.strip().startswith("</way"):
            inWay = False
            names = []
            prevnd = ''
        elif inWay:
            if line.strip().startswith("<nd"):
                #register connection
                s = line.split('"')
                if prevnd == '':
                    pass
                else:
                    AL[s[1]][prevnd] = 0
                    AL[prevnd][s[1]] = 0
                    names.append((s[1],prevnd))
                    SN[s[1]][prevnd] = 'NoName'
                    SN[prevnd][s[1]] = 'NoName'
                prevnd = s[1]
            elif line.strip().startswith('<tag k="name"'):
                xxy = line.split("v=")
                nm = xxy[1].split('"')[1]
                for cn in names:
                    SN[cn[0]][cn[1]] = nm
                    SN[cn[1]][cn[0]] = nm
                    
    for n in AL.keys():
        for nn in AL[n].keys():
            AL[n][nn] = pythg(N[n],N[nn])
##    jjj = 1
##    for x in AL.keys():
##        print (x, AL[x])
##        jjj += 1
##        if jjj > 200:
##    ##        pass
##            break
    return (AL, SN)



##jjj = 1
##for x in AL.keys():
##    print (x, AL[x])
##    jjj += 1
##    if jjj > 200:
####        pass
##        break





