import hashlib
import time

if __name__=="__main__":
    st = time.process_time()
    c = "1000000000000000"
    hashedC = "6a4ef24cb01aa0e97da4186c067128b828532db703db8872fa736a0cc0b363b1" #sha256 of 1000000000000000
    knownHash = " your hash here "
    #while (c != "1000000010000000"):
    while (hashedC != knownHash):
        c = int(c)
        c = c+1
        c = str(c)
        hashedC = hashlib.sha256(c.encode('ascii')).hexdigest()
        print(c + ' - ' + hashedC)
    else:
        print(c + ' - ' + hashedC)
        print("HASH MATCH")
    print(c)
    et = time.process_time()
    res = et - st
    print('CPU Execution time:', res, 'seconds')