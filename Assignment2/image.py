import os
import sys
import time
import pathlib
#detect if the image_service txt had any input. If so, put a path according to the input


dirs = os.listdir("images")
#file = open(os.path.join(sys.path[0], "image_service.txt"), "w+") 
while(True):
    time.sleep(1)
    file = open(os.path.join(sys.path[0], "image_service.txt"), "r+")
    input = file.read()
    if(input != ""):
        try:
            if(int(input) >= len(dirs)):
                input = int(input)
                input = input % len(dirs)
        except:
            continue
        print(dirs[int(input)])
    file.seek(0)
    file.truncate()
    #put the dirs inthe file
    file.write(str(dirs[int(input)]))
    file.close()
    time.sleep(2)
    #test
    file = open(os.path.join(sys.path[0], "image_service.txt"), "r")
    file.seek(0)
    print(str(file.read()))
    file.close()
    



# while(True):
#     input = file.read()
#     #check if there is anyinput
#     if(input == "end"):
#         file.seek(0)
#         file.truncate()
#         file.close()
#         break
#     if(input != ""):
#         file.seek(0)
#         file.truncate()
#         if(int(input) >= len(dirs)):
#             input = int(input)
#             input = input % len(dirs)
#         path = f"{path}\{dirs[int(input)]}"
#         file.seek(0)
#         file.truncate()
#         file.write(path)

    
        
