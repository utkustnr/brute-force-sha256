import math

startingPoint = 1000000000000000
imei = YOURIMEIHERE
algoOEMcode = 1000000000000000

def algoIncrementChecksum(imei, checksum, genOEMcode):
    genOEMcode  += int(checksum + math.sqrt(imei) * 1024)
    return genOEMcode

def luhn_checksum(imei):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(imei)
    oddDigits = digits[-1::-2]
    evenDigits = digits[-2::-2]
    checksum = 0
    checksum += sum(oddDigits)
    for i in evenDigits:
        checksum += sum(digits_of(i * 2))
    return checksum % 10

def algoIncrementChecksum(imei, checksum, genOEMcode):
  genOEMcode  += int(checksum + math.sqrt(imei) * 1024)
  return genOEMcode

def luhn_checksum(imei):
  def digits_of(n):
    return [int(d) for d in str(n)]
  digits      = digits_of(imei)
  oddDigits   = digits[-1::-2]
  evenDigits  = digits[-2::-2]
  checksum    = 0
  checksum    += sum(oddDigits)
  for i in evenDigits:
    checksum += sum(digits_of(i * 2))
  return checksum % 10

checksum = luhn_checksum(imei)
with open("codes.txt", "w") as f:
    while (len(str(algoOEMcode)) < 22):
        if (len(str(algoOEMcode)) == 16):
            algoOEMcode = algoIncrementChecksum(imei, checksum, algoOEMcode)
            f.write("\n")
            f.write(str(algoOEMcode))
        elif (len(str(algoOEMcode)) == 17):
            algoOEMcode = algoIncrementChecksum(imei, checksum, algoOEMcode)
            first=str(algoOEMcode)[1:]
            last=str(algoOEMcode)[:-1]
            f.write("\n")
            f.write(str(first))
            f.write("\n")
            f.write(str(last))
        elif (len(str(algoOEMcode)) == 18):
            algoOEMcode = algoIncrementChecksum(imei, checksum, algoOEMcode)
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            f.write("\n")
            f.write(str(first))
            f.write("\n")
            f.write(str(last))
        elif (len(str(algoOEMcode)) == 19):
            algoOEMcode = algoIncrementChecksum(imei, checksum, algoOEMcode)
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            f.write("\n")
            f.write(str(first))
            f.write("\n")
            f.write(str(last))
        elif (len(str(algoOEMcode)) == 20):
            algoOEMcode = algoIncrementChecksum(imei, checksum, algoOEMcode)
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            f.write("\n")
            f.write(str(first))
            f.write("\n")
            f.write(str(last))
        elif (len(str(algoOEMcode)) == 21):
            algoOEMcode = algoIncrementChecksum(imei, checksum, algoOEMcode)
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            first=str(algoOEMcode)[1:]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            last=str(algoOEMcode)[:-1]
            f.write("\n")
            f.write(str(first))
            f.write("\n")
            f.write(str(last))
        else:
            print("Time to go to bed granpa")