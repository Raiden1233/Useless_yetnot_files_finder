import os
import time

# Specify the directory to traverse
directory2 = input("In Case you don't know; What Directory looks like here is an exp\nExample 'C:\\Users\\Home\\Desktop'\nEnter The Directory or Location to check all the files on that Directory.\n---->  ")

directory2 = directory2.replace("\\", "/")

for direcotry2,dirs,filename in os.walk(directory2, topdown= True):
    choose = ["1: Your Current Directory" , "2: Your Sub Directory", "3: Your Items in current directory" , "4: All 3"]
    user = input(f"\nWhat you would like to see here, Chose one of following options.\n{choose[0]}\n{choose[1]}\n{choose[2]}\n{choose[3]}\n--->  ")
    time.sleep(1)
    if user ==  "1":
        print(f"Your Directory: {directory2}") 
    elif user == "2":
        print(f"Sub Directory{dirs}")
    elif user == "3":
        print(f"Items: {filename}")
    elif user == "4":
        print(f"Your Directory: {directory2}")
        print()
        time.sleep(1) 
        print(f"Sub Directory{dirs}")
        print()
        time.sleep(1)
        print(f"Items: {filename}")
    print("\n________________________________")    
    print("\nYou entered in your Sub Directory\n")
    print("__________________________________")


userinput = input("Press q to quit\n---> ")

while(userinput != "q"):
    userinput = input("Press q to quit\n---> ")
    time.sleep(1)
    if userinput == "q":
        quit
