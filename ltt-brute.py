import hashlib
import itertools

def hashcheck(code):
    hashedC = hashlib.sha256(code.encode('ascii')).hexdigest()
    print(code + ' - ' + hashedC)
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
    
    print("Hope you have terabyte of ram just like linus, bud")
    combinedlist = []
    combinedlist = [''.join(x) for x in itertools.product(revlist, plainlist)]
    revlist = []
    plainlist = []
    shalist = []
    print("Hard part is done, starting code tests.")
    for code in combinedlist:
        shalist.append(code.rstrip())
        hashedC = hashcheck(code)
        if (hashedC != knownHash):
            shalist.remove(code)
            print("Not" + code)
        else:
            print(shalist)
            print(code + hashedC)
            print("HASH MATCH")