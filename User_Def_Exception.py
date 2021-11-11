import sys

class Error(Exception):
    pass

class ValueSmall(Exception):
    pass

class ValueLarge(Exception):
    pass

num=10
while True:
    try:
        in_num=int(input("Enter Number"))

        if in_num < num:
            raise ValueSmall

        elif in_num > num:
            raise ValueLarge

        break

    except ValueSmall:
        print("This Value is Too Small")
        print()
    
    except ValueLarge:
        print("The Value is Too Large")
        print()

print("Congo!!,You Guessed it Correctly")