import sys
randomlist=['a',0,2]

for entry in randomlist:
    try:
        print("The Entry is",entry)
        r=1/int(entry)
        break

    except:
        print("OOPS!",sys.exc_info()[0],"Occured")
        print("Next Entry")
        print()

    finally:
            print("Hello")


print("The Reciprocal of ",entry,"is",r)


