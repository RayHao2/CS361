import random
import os
import sys
import time
#running process
while(True):
    userInput = input("Enter 1 to get a random image or 2 to exist the program: ")
    if(int(userInput) == 1):
        
        #getting number from the PRNG.py
        file = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "r+") 
        file.seek(0)
        file.write("run")
        file.seek(0)
        time.sleep(0.5)
        imageNumber = file.read()
        #print(imageNumber)
        file.close()

        #getting images from the image.py
        file = open(os.path.join(sys.path[0], "image_service.txt"), "w+") 
        file.seek(0)
        #calling the image.py
        file.write(str(imageNumber))
        time.sleep(1.5)
        #get the path
        path = str(file.read())
        print(path)
        file.close()
    else:
        #end image.py 
        file = open(os.path.join(sys.path[0], "image_service.txt"), "w+") 
        file.seek(0)
        file.write("end")
        #end PRNG.py
        file = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "r+") 
        file.seek(0)
        file.write("end")
        break
