import random
import os
import sys
import time
#running process



while(True):
    userInput = input("Enter 1 to get a random image or 2 to exist the program: ")
    if(int(userInput) == 1):
        
        #getting number from the PRNG.py
        fileN = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "w+") 
        fileN.seek(0)
        fileN.write("run")
        fileN.seek(0)
        time.sleep(5)
        imageNumber = fileN.read()
        print(imageNumber)
        fileN.close()

        
        #send number to image.py
        time.sleep(1)
        fileI = open(os.path.join(sys.path[0], "image_service.txt"), "w+") 
        fileI.write(str(imageNumber))
        #time.sleep(5)
        fileI.close()

        # time.sleep(5)
        # fileI =open(os.path.join(sys.path[0], "image_service.txt"), "r") 
        # print(fileI.read())
        # fileI.close()
    else:
        #end image.py 
        #file.seek(0)
        fileI = open(os.path.join(sys.path[0], "image_service.txt"), "w+") 
        fileI.write("end")
        fileI.close()
        #end PRNG.py
        fileN = open(os.path.join(sys.path[0], "PRNG_Service.txt"), "w+") 
        fileN.seek(0)
        fileN.write("end")
        fileN.close()
        break

