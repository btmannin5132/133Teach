def ifGeneral():
    a = 5
    b = 7
    if a == 5:
        print("a = 5")
    
    print("I display no matter what")

    if b == 7:
        print("b = 7")


def nestIf():
    a = 5
    b = 7

    if a == 5:
        print("a = 5")
        if b > 10:
            print(f"b is {b}")

        else:
            print("b <= 10")

        print("I will still run as long as a == 5")

    print("I will print no matter what")


def ifElse():
    a = 5
    b = 7

    if a > b:
        print("a is greater than b")
        return a
    elif b > a:
        print("b is greater than a")
        return b
    else:
        print("a = b")
        return a

def main():
    ifGeneral()
   # nestIf()
   # ifElse()

if __name__ == "__main__": # if this is the file being executed (instead of being imported):
    main()