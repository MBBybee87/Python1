# Title: ccpin.py
#
# Created by: Matthew Bybee
# Date: 03/10/2019, 7:10pm
# Version 1.1
# 
# Purpose: To accept a pin and check for a match

import errno, sys

#valid_input definition
def valid_input(pin):

    if(pin == "1234"): #Remember to run this as a string check
        print("Your PIN is correct")
        return True

    elif(pin.isdigit() == False):
        print("Your PIN is incorrect (BAD FORMAT).")
        print("Correct format is: <9876>")
        return False

    elif(len(str(pin)) != 4): #must convert to s string before len() works
        print("Your PIN is incorrect (BAD FORMAT)")
        print("Correct format is: <9876>")
        return False

    else:
        print("Your PIN is incorrect")
        return False



#main definition
def main():

    i = 0 #for while loop
    pin = 9999
    loop = False #Should the loop break or not

    while(i < 3):
        #Accept user input
        pin = input("Enter your Pin: ")
        
        #Check if valid_input() returns true
        if(valid_input(pin) == True):
            sys.exit(0)

        #if it returns False, increment i
        else:
            i += 1
            
            #exit program if 3 failures
            if(i == 3):
                print("Your bank card is blocked")
                sys.exit(1)
            #else, continue normally
            continue
