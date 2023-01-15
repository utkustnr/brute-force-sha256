import hashlib
import itertools

def hashcheck(line):
    hashedC = hashlib.sha256(line.encode('ascii')).hexdigest()
    print(line + ' - ' + hashedC)
    return hashedC

if __name__ == '__main__':

    hashedC = "6a4ef24cb01aa0e97da4186c067128b828532db703db8872fa736a0cc0b363b1" # don't touch
    knownHash = " " # do touch

    revlist =[]
    r = "99999999"
    print("Doing revlist")
    while (str(r) != "00000000"):
        r = int(r)
        r = r-1
        r = str(r)
        if len(r) < 8:
            r = f'{r:0>8}'
        revlist.append(r.rstrip())
    else:
        print(r)
        print("Revlist done")

    plainlist =[]
    p = "00000000"
    print("Doing plainlist")
    while (str(p) != "99999999"):
        p = int(p)
        p = p+1
        p = str(p)
        if len(p) < 8:
            p = f'{p:0>8}'
        plainlist.append(p.rstrip())
    else:
        print(p)
        print("Plainlist done")
    
    print("Starting combination")
    with open("combined.txt", 'w', encoding='ascii') as file:
        for r in plainlist:
            print(r + "________")
            for p in revlist:
               file.write(r.strip()+p.strip()+"\n")
            print(r + "done")

    print("Starting hashing")
    with open("combined.txt", 'r', encoding='ascii') as file:
        shalist =[]
        for line in file:
            shalist.append(line.rstrip())
            hashedC = hashcheck(line)
            if (hashedC != knownHash):
                shalist.remove(line)
                print("Not" + line)
            else:
                print(shalist)
                print(line + hashedC)
                print("HASH MATCH")