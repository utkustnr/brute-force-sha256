import hashlib

def hashcheck(line):
    hashedC = hashlib.sha256(line.encode('ascii')).hexdigest()
    print(line + ' - ' + hashedC)
    return hashedC

if __name__ == '__main__':

    hashedC = "6a4ef24cb01aa0e97da4186c067128b828532db703db8872fa736a0cc0b363b1" # don't touch
    knownHash = " " # do touch

    revlist =[]
    r = "99999999"
    print("Cycling Rev")
    while (str(r) != "00000000"):
        r = int(r)
        r = r-1
        r = str(r)
        if len(r) < 8:
            r = f'{r:0>8}'
        if ("99" in r):
            r = r.replace("99", "98")
        if ("88" in r):
            r = r.replace("88", "87")
        if ("77" in r):
            r = r.replace("77", "76")
        if ("66" in r):
            r = r.replace("66", "65")
        if ("55" in r):
            r = r.replace("55", "54")
        if ("44" in r):
            r = r.replace("44", "43")
        if ("33" in r):
            r = r.replace("33", "32")
        if ("22" in r):
            r = r.replace("22", "21")
        if ("11" in r):
            r = r.replace("11", "10")
        p = "00000000"
        print("Cycling Plain")
        while (str(p) != "99999999"):
            p = int(p)
            p = p+1
            p = str(p)
            if len(p) < 8:
                p = f'{p:0>8}'
            combined = (r.strip()+p.strip())
            hashedC = hashcheck(combined)
            if (str(hashedC) != str(knownHash)):
                pass
            if (str(hashedC) == str(knownHash)):
                print(combined + hashedC)
                print("HASH MATCH")
                quit()