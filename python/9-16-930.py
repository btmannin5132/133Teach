#Code generated in class during 9:30 section on 9/16
def regionCheck():
    y = .25
    x = .75

    if y == 1-x:
        print("On the line")
    elif y < 1-x:
        print("Region 1")
    else:
        print("Region 2")
        

def main():
    regionCheck()

if __name__ == "__main__": # if this is the file being executed (instead of being imported):
    main()