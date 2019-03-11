import errno, sys

def valid_input(pin):
    if (pin == "1234"):
        print("Your PIN is correct")
        return True
    elif (pin.isdigit() == False):
        print("Your PIN is incorrect (BAD FORMAT).")
        print("Correct format is: <9876>")
        return False
    elif (len(str(pin)) != 4):
        print("Your PIN is incorrect (BAD FORMAT)")
        print("Correct format is: <9876>")
        return False
    else:
        print("Your PIN is incorrect")
        return False

def main():
    i = 0
    pin = 9999
    loop = False

    while (i < 3):
        pin = input("Enter your Pin: ")
        if(valid_input(pin)== True):
            sys.exit(0)
        else:
            i += 1
            if(i == 3):
                print("Your bank card is blocked")
                sys.exit(1)
            continue
