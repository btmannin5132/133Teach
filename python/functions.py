def dispText(text):
    print(f"The text to be displayed is: {text}")

def main():
    print("This is the main function")
    text2Display = "Ben"
    dispText(text2Display)





if __name__ == "__main__": # if this is the file being executed (instead of being imported):
    print("This will run without being in a function.")
    main()