def for1():
    for x in [7,9,16]:
        y = x+2
        print(f"x={x}, y={y}")

def for2():
    for x in range(1,10):
        y = x**2
        print(f"x={x}, y={y}")

def forList():
    a=range(10)
    List1 = []
    for x in a:
        List1.append(x+4)
        #print(List1)
    #print(List1)

def nestFor():
    a_V = []
    for ii in range(1,3):
        for jj in range(1,6,2):
            z = ii + jj
            a_V.append(z)
            print(f"ii:{ii}, jj:{jj}, a_V:{a_V}")

def leaveLoop():
    numbers = [1, 2, 3, 5, 7, 10, 15, 22, 25, 28]
    for num in numbers:
        if num > 20:
            print("Found a number greater than 20!")
            break
        elif num % 5 == 0:
            continue
        elif num == 2:
            pass
        else:
            print(num)


if __name__ == "__main__": # if this is the file being executed (instead of being imported):
    for1()
    #for2()
    #forList()
    #leaveLoop()