def while1():
    x = 1
    while x <= 5:
        #add 1 to x (yes, you can use the same variable to assign)
        x = x + 1
        #calculate y
        y = x**2 - 1
        #print
        print(f"x={x} y={y}")
    #After the loop:    
    z = x * y
    print(f"z={z}")

def while2():
    count_loops = 0
    x = 1
    while x <= 5:
        x = x + 1
        y = x**2 - 1
        count_loops += 1
        print(f"x={x} y={y}")
    # Display counter outside loop​
    print(f"Counter = {count_loops}")

def while3(): #stuck in a loop
    count_loops = 0
    x = 1
    while x <= 5:
        x = x
        y = x**2 - 1
        count_loops += 1
        print(f"x={x} y={y}")
    # Display counter outside loop​
    print(f"Counter = {count_loops}")


if __name__ == "__main__": # if this is the file being executed (instead of being imported):
    while1()
    #while2()
    #while3()