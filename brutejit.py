from numba import jit, cuda
import hashlib
import time

@jit(target_backend='cuda', forceobj=True)
def func(c,hashedC,knownHash):
    #while (c != "1000000010000000"): #for benchmark
    while (hashedC != knownHash):
        c = int(c)
        c = c+1
        c = str(c)
        hashedC = hashlib.sha256(c.encode('ascii')).hexdigest()
        print(c + ' - ' + hashedC)
    else:
        print(c + ' - ' + hashedC)
        print("HASH MATCH")
        return c

if __name__=="__main__":
    c = "1000000000000000"
    hashedC = "6a4ef24cb01aa0e97da4186c067128b828532db703db8872fa736a0cc0b363b1" #sha256 of 1000000000000000
    knownHash = " your hash here "
    st = time.process_time()
    code = func(c,hashedC,knownHash)
    print(code)
    et = time.process_time()
    res = et - st
    print('JIT Execution time:', res, 'seconds')