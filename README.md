# brute-search-sha256
Bunch of scripts to find out 16 digit number from sha256 digest.

I initially created these because I lost my android's bootloader unlock code and I had nvme partition backup which had sha256 of bootloader code inside. 

- No, I can't request code from manufacturer because huawei.
- No, I don't want to open back cover.
- I know these scripts could be better but I literally wrote one, didn't liked it then started another from scratch again over the course of half an hour. I don't want to waste 5 more minutes writing another, it's already running in background as I type.

How to use?

- You need to have a hash of 16 digit number. (could be tweaked to suit your needs, 16 is what I needed at the time)
- Linux environment if using bruteimei.py, hashgenforimei.sh bruteba.sh
- Python <3.11 (for numba) if using brutecpu.py, bruteimei.py,brutejit.py
- Edit the scripts and add your own hash or imei.

bruteba.sh : Basically keeps increasing number until it's hash is matched with the hash you need.

brutecpu.py : Best iteration. Same as bruteba.sh but faster.

bruteimei.py : Takes luhn checksum of imei into account and creates codes accordingly but after a while it starts generating 17 and more digits so my response 
to that was to delete first digit for one variable, delete last digit for one variable then save both into file. File it generates becomes too big to open at 
some point so I didn't even consider fixing it. Oh I stole the code btw.

brutejit.py : Basically a failed attempt at making brutecpu.py gpu accelerated. Apperantly you can't use hashlib inside numba. If you do it falls back to object mode which is basically same as brutecpu.py but slower. I tried rewriting whole hashing function from scratch for it but gave up eventually.

hashgenforimei.sh : Just a simple bash script to generate hashes for each line in a text file. Made it for bruteimei.py. After getting codes.txt you pass it to this script as an argument and it generates hashes.txt.
