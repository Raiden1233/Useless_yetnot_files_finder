import os
import time

# Specify the directory to traverse
directory2 = input("Enter your directory where you want to search items in\n\nRemember to put r before pasting your directory.\n----> ")

directory2 = directory2.replace("\\", "/")

for direcotry2,dirs,filename in os.walk(directory2, topdown= True):
    time.sleep(1)
    print(f"Your Directory: {directory2}")
    print("___________________________")
    time.sleep(1)
    print(f"Sub Directory{dirs}")
    print("___________________________")
    time.sleep(1)
    print(f"Items: {filename}")
    print("___________________________")


userinput = input("Press q to quit\n---> ")

while(userinput != "q"):
    userinput = input("Press q to quit\n---> ")
    time.sleep(1)
    if userinput == "q":
        quit
