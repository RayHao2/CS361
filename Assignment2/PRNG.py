#read form PRNG_Service.txt that if run exists 

import random
import os
import sys
import time

while(True):
    file = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "r+") 
    input = file.read()
    #if the file have run on it, generate a random number

    if input == "run":
        file.seek(0)
        file.truncate()
        num = random.randint(0,9)
        file.write(str(num))
    if input == "end":
        file.seek(0)
        file.truncate()
        break
    file.close
#time.sleep(1)