#read form PRNG_Service.txt that if run exists 

import random
import os
import sys

# fileR = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "r") 


# input = fileR.read()
# fileR.close
# #if the file have run on it, generate a random number

# fileW = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "w") 
# if input == "run":
#     num = random.randint(0,9)
#     print(num)
#     fileW.write(str(num))
    

# fileW.close
while(True):
    fileR = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "r") 
    input = fileR.read()
    fileR.close
    #if the file have run on it, generate a random number

    fileW = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "w") 
    if input == "run":
        num = random.randint(0,9)
        print(num)
        fileW.write(str(num))
    if input == "end":
        fileW.write("")
        break
    fileW.write("")
    fileW.close