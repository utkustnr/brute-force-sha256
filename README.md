# brute-search-sha256
Bunch of scripts to find out 16 digit number from sha256 digest.

I initially created these because I lost my android's bootloader unlock code and I had nvme partition backup which had sha256 of bootloader code inside.

> Why didn't you ____ ?

- No, I can't request code from manufacturer because huawei.
- No, I don't want to open back cover.
- I know it will take a long time. In fact going from 1000000000000000 to 9999999999999999 will take 10416666 full days at rate of 10000 iterations per second but I'm not going from start to finish. I did some guesswork before running the script.
- I know these scripts could be better but I literally wrote one, didn't liked it then started another from scratch again over the course of half an hour. I don't want to waste 5 more minutes writing another, it's already running in background as I type. *update: Wrote 2 more. You going to need either too much ram or too much storage for these.*

> How to use?

- You need to have a hash of 16 digit number. (could be tweaked to suit your needs, 16 is what I needed at the time)
- Linux environment if using bruteimei.py, hashgenforimei.sh, bruteba.sh
- Python <3.11 (for numba)
- If you want to cut short, you're gonna need ram, lots of ram. Or storage. Depending on which one you choose.
- Edit the scripts and add your own hash or imei.

> Which one to use?

sane-brute.py : This is what you'd want to use probably. Uses sensible amount of ram and does the job noticably faster than others. Splits 16 digit number into 8 digit 2 chunks and saves each into a list. Then combinetes 2 list against each other and write results to a file. Hashing function takes each line as an input. Could take up a lot of space but uses less ram.

alternate-brute.py : Another shortcut attempt. If you know that the number you're looking for has no duplicate (eg. 99, 88, 77) digits then this might help out a little.

brutecpu.py : Second best that doesn't consume huge chunks of memory or space. Same as bruteba.sh but faster.

brutejit.py : Basically a failed attempt at making brutecpu.py gpu accelerated. Apperantly you can't use hashlib inside numba. If you do it falls back to object mode which is basically same as brutecpu.py but slower. I tried rewriting whole hashing function from scratch for it but gave up eventually.

bruteba.sh : Basically keeps increasing number until it's hash is matched with the hash you need.

bruteimei.py : Takes luhn checksum of imei into account and creates codes accordingly but after a while it starts generating 17 and more digits so my response 
to that was to delete first digit for one variable, delete last digit for one variable then save both into file. File it generates becomes too big to open at 
some point so I didn't even consider fixing it. Oh I stole the code that takes imei to account btw.

hashgenforimei.sh : Just a simple bash script to generate hashes for each line in a text file. Made it for bruteimei.py. After getting codes.txt you pass it to this script as an argument and it generates hashes.txt.

ltt-brute.py : Unless you have terabyte of ram like linus from linustechtips, stay away. Even with 12 digit AND 180 gb of page file it gave memory error. Server grade.
