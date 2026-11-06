import os
from time import sleep

def clear_ter() :
    os.system("cls")
    

# 1:31:25
def timer(t):
    try :
        t = t.split(":") # Example, input = 01:22:31 -> ["1","22","31"]
        h = int(t[0]) # Hour
        m = int(t[1]) # Minute
        s = int(t[2]) # Seccond
        print(f"\n{h}:{m}:{s}") # Printing input
        while (h+m+s) != 0 : # if hour and minute and seccond equal to zero the loop will break
            if s == 0 and m != 0 : # When s - 1 == 0, and min != 0 , the minute number will be 59
                s = 59
                m -= 1
            elif m == 0 and h != 0 and s == 0 : # When m = 0, and h != 0 and s = 0, minute and seccond will be 59 and houre = houre - 1
                m = 59
                s = 59
                h -= 1
            else : # Main work
                s -= 1 
            sleep(1) # Stop for 1s 
            print(f"{h}:{m}:{s}")
        print("\n>> Timer finished !\n")
    except :
        print("\n>> Invalid Time !\n- Enter like (00:00:00)\n")

# Main Func
def main() :
    while True :
        t1 = input("Enter your time (00:00:00) : ")
        if t1 == "" : break
        timer(t1)

if __name__ == "__main__" :
    main()
    print("\n~ Thanks for choosing us ;)\n")