import random
import os
import sys
import time

file = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "w+") 
file.seek(0)
file.write("run")
file.seek(0)
time.sleep(0.5)
randN = file.read()
print(randN)
file.close()
