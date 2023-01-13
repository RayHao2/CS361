#read form PRNG_Service.txt that if run exists 

import random
import os
import sys
import time

while(True):
    file = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "r+") 
    input = file.read()
    #if the file have run on it, generate a random number
    if input == "end":
        file.seek(0)
        file.truncate()
        file.close()
        break
    if input == "run":
        file.seek(0)
        file.truncate()
        num = random.randint(0,9)
        file.write(str(num))
#time.sleep(1)