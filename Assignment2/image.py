import os
import sys
import time

#detect if the image_service txt had any input. If so, put a path according to the input


path = r"C:\Users\haoju\OneDrive\Desktop\CS361\Assignment2\images"
dirs = os.listdir(path)
file = open(os.path.join(sys.path[0], "image_service.txt"), "w+") 
while(True):
    input = file.read()
    #check if there is anyinput
    if(input == "end"):
        file.seek(0)
        file.truncate()
        file.close()
        break
    if(input != ""):
        file.seek(0)
        file.truncate()
        if(int(input) >= len(dirs)):
            input = int(input)
            input = input % len(dirs)
        path = f"{path}\{dirs[int(input)]}"
        file.seek(0)
        file.truncate()
        file.write(path)

    
        
