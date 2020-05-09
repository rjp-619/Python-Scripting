import os   #import module type


print(os.getcwd())          #get the current working directory

os.chdir("/home/rajas")     #change directory

print(os.getcwd())


os.mkdir("/home/rajas/ll")      #make new folder location
os.rmdir("/home/rajas/ll")      #delete the folder

#os.remove("/home/rajas/ll.txt")    #remove the file in mentioned location



print(os.path.join("FIRST LOCATION", "SECOND LOCATION"))        #joins two path directories

print(os.path.split("GIVE ONE PATH"))       #it will split according to the the exixting path



print(os.path.exists("GIVE PATH location"))     #this returns true or false


