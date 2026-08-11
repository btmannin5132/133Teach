# A GLOBAL variable, accessible everywhere.
menu_item = "egg and spam"

def order():
    # This is a LOCAL variable. It only exists inside this function.
    customer_item = "spam, egg, sausage, and spam"
    print(f"Customer: I'll have the {customer_item}.")
    print(f"Waitress: We've only got {menu_item}, sir. Waiting on more spam")
    print("Customer: Oh, alright then.")

def serves():
    # The waitress uses the GLOBAL variable because that's what's available
    # to the whole restaurant.
    print(f"Waitress serves: Here's your {menu_item}, sir. The one from the menu.")

def request():
    menu_item = "spam, egg, spam, spam, spam, bacon, and spam"
    print(f"Customer: How much spam does {menu_item} have in it?")
    print(f"Waitress: Not as much as spam, spam, spam, spam, spam, baked beans, spam and spam has.")

def delivery():
    # This function uses the 'global' keyword to change the GLOBAL menu_item.
    # It's a special delivery of 'spam spam spam spam'.
    global menu_item
    menu_item = "spam, spam, spam, spam, egg and spam"
    print("We got more spam!")

# Here's what happens:

print(f"The menu has been set up. The menu has {menu_item}, and that's it")

print("\nA customer comes in and places an order.")
order()

print("\nThe waitress serves from the menu again.")
serves()

print("\nThe new spam delivery arrives!")
delivery()

print("\nNow, let's see what's on the menu after the delivery.")
serves()

print("\nPerhps something a little off menu?")
request()

#Moral of the story: Don't modify global varables inside of functions if you can avoid it...
#Globals are great for:
    #Pins on microcontrollers
    #motor assignments
    #Set variables that a lot of places will use, but don't need to be changed

#Don't use globals for:
    #Literally anything else...
