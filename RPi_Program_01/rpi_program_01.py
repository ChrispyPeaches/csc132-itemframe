######################################################################
# Name:         Chris Perry
# Date:         4/4/22
# Description:  A text-based game that puts a user in a mansion with 4 rooms.
#                   - There exists a puzzle.
#                       - A door requires a phrase to be deciphered
#                       - The phrase is changeable and randomly encrypted.
#                       - On successful entry of the deciphered phrase,
#                           the user goes outside the house and wins
#                       - When the user wins the game a trophy displays
#                   - There exists a couple of hints around the house.
#                       - There is a book of ciphers that lists a few
#                           cipher methods as chapters.
#                       - There is a six-pack that has an encrypted brand.
#                           - Decrypted, this brand is "Mueller's"
#                               - This is a reference to the German surname
#                                   "Mueller" being connected to the surname
#                                   "Miller".
#                   - There exists an exit through a window that ends the game.
#                       - When they loose the game, a skull displays.
######################################################################
######################################################################
from random import randint

#####################
## ADDED FUNCTIONS ##
#####################
#   This function takes the door's puzzling phrase and creates a caesar cipher of a random character
#       shift amount, then returns the value of the encoded phrase as a string.
#       - It does this by taking a list of all alphabetic characters, one for upper case, one for lower case
#           and shifts it by a random amount with a possible range of [3,7] shifted characters, then converts
#           the characters to a string.
#           - To account for wrapping around from z to a in the alphabetic lists, uses the mod operator
#               in order to find how many letters it needs to shift after wrapping around to a in the list
#       - I also added future proofing to be able to randomize which cipher is used if more possible ciphers
#           are added, such as the ones listed in the "book" item in one of the rooms. Any cipher used is to be
#           added to the description of the "book" item.
def encode():
    global passphrase
    passphrase = "example phrase"
    encoding = 'caesar'
    
    if (encoding == 'caesar'):
        inpt = passphrase
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabetl = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(0,randint(3,7)):
            output = [0 for i in range(len(inpt))]
            for j in range(0,len(inpt)):
                for k in range(0,26):
                    if(inpt[j] == alphabet[k]):
                        output[j] = alphabet[(k+i) % len(alphabet)]
                        if (inpt[j] == "Z"):
                            print(f"{output[j]}, {(k+i) % len(alphabet)}")
                    elif(inpt[j] == alphabetl[k]):
                        output[j] = alphabetl[(k+i) % len(alphabet)]
                        if (inpt[j] == "z"):
                            print(f"{output[j]}, {(k+i) % len(alphabet)}")
                    elif inpt[j] == "'" or inpt[j] == ",":
                        output[j] = inpt[j]
                    elif inpt[j] == " ":
                        output[j] = inpt[j]
            s = ""
            for spot in output:
                s += str(spot)      
    return s

#   This funciton creates the door puzzle where the cipher is implemented.
#   - The user is told a phrase and is instructed to decipher the phrase. They'll be able to find
#       a list of ciphers in the "book" item in Room 3
#   - The door gives different responses based on success and how many times the user has accessed
#       the door to decrease annoyance with the puzzle
#   - I got this idea from a D&D puzzle for my campaign I created with similar attributes
#   - If the user puts in the correct deciphered phrase, the function returns True, otherwise False
#       - This tells the "go" verb if-then statement whether the user succeeded or not
def door():
    global doorAttempts
    if (doorAttempts == 0):
        print(f"The Door speaks,\n'Don't be brash, solve my puzzle in order to pass. Decipher this phrase.\n{encodedPhrase}")
    else:
        print(f"Decipher this phrase.\n{encodedPhrase}")
    inpt = input()
    if(inpt == passphrase):
        return True
    else:
        if(doorAttempts < 3):
            print("\nThe Door speaks, 'Invalid. Come back and try again. There might be a clue somewhere.'")
        else:
            print("\nThe Door speaks, 'Invalid. You might wanna look for clues in Room 3'")
        input("\nPress any key to continue.")
        return False

#   This function just prints a ASCII trophy image and a message when the user wins
#       - runs when the user wins the game (solves the door puzzle)

def win():
    print(
        """
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `-------`
                 
        Congratz! You made it out!        
        """
    )


# the blueprint for a room
class Room:
# the constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self.grabbablesDescriptions = []    # Array for descriptions of grabbables

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value
    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    #   Accessor and Mutator for descriptions of grabbables
    @property
    def grabbablesDescriptions(self):
        return self._grabbablesDescriptions
    @grabbablesDescriptions.setter
    def grabbablesDescriptions(self, value):
        self._grabbablesDescriptions = value
    
    
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made
    # of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item, desc):
        # append the item to the list
        self._grabbables.append(item)
        self._grabbablesDescriptions.append(desc)    # Adds descriptions to grabbable items

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s


######################################################################
# creates the rooms
def createRooms():
    # r1 through r4 are the four rooms in the mansion
    # currentRoom is the room the player is currently in (which can
    # be one of r1 through r4)
    # since it needs to be changed in the main part of the program,
    # it must be global
    global currentRoom
    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Outside")    # Adds a room named "outside" listed as r5.

    ############
    ## ROOM 1 ##
    ############
    # add exits to room 1
    r1.addExit("east", r2) # -> to the east of room 1 is room 2
    r1.addExit("south", r3)
    r1.addExit("door", r5)
    # add grabbables to room 1
    r1.addGrabbable("key", "A golden key. Doesn't look like it'll decipher anything.")
    # add items to room 1
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")

    ############
    ## ROOM 2 ##
    ############
    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    # add items to room 2
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes.")

    ############
    ## ROOM 3 ##
    ############
    # add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    # add grabbables to room 3
    r3.addGrabbable("book", "It's a book of ciphers. Chapters: Caesar, Vigenère, Pigpen, and Playfair")
    # add items to room 3
    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "There is nothing special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")

    ############
    ## ROOM 4 ##
    ############
    # add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None) # DEATH!
    # add grabbables to room 4
    r4.addGrabbable("6-pack", "It read's the brand 'Jrbiibo'p'. You recognize the graphics to be the 'Mueller's' Brand")
    # add items to room 4
    r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")
    # set room 1 as the current room at the beginning of the game
    currentRoom = r1

# Displays message and ASCII image when the player dies.
# yes, this is intentionally obfuscated!
# Made the skull image more intelligable and digestable when programming and running the game.
def death():
    print(
        """
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$'   '$$$'   '$$$$$$u
       '$$$$'      u$u       $$$$'
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         '$$$$uu$$$   $$$uu$$$$'
          '$$$$$$$'   '$$$$$$$'
            u$$$$$$$u$$$$$$$u
             u$'$'$'$'$'$'$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      '$$$$$$$$$'     uu$$$$$$
u$$$$$$$$$$$uu    '''''    uuuu$$$$$$$$$$
$$$$'''$$$$$$$$$$uuu   uu$$$$$$$$$'''$$$'
 '''      ''$$$$$$$$$$$uu ''$'''
           uuuu ''$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ''$$$$$$$$$$$uuu$$$
  $$$$$$$$$$''''           ''$$$$$$$$$$$'
   '$$$$$'                      ''$$$$''
     $$$'                         $$$$'
        """
    )
    print("\n\nYou jumped out of a window, for some reason, and died. . . .")
    

######################################################################
# START THE GAME!!!

doorAttempts = 0            #   Keeps track of how many times the user accessed the door function
encodedPhrase = encode()    #   Encodes the given phrase for the puzzle and stores it

inventory = [] # nothing in inventory...yet
inventoryDesc = []  #   Adds a container to store descriptions of items and grabbables in the inventory
createRooms()  # add the rooms to the game
# play forever (well, at least until the player dies or asks to quit)
while (True):
    # If the current room is None (and the player is dead), exit the
    #   game
    if (currentRoom == None):
        death()
        exit()
    # If the current room is "Outside", you've won. Exit the game
    if (currentRoom.name == "Outside"):
        win()
        exit()
    
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom,inventory)
    
    # display the status
    print("========================================================")
    print(status)

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    action = input("What to do? ")
    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()
    # exit the game if the player wants to leave (supports quit,
    # exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break
    # set a default response
    response = "I don't understand.  Try verb noun.  Valid verbs are go, look, and take"
    # split the user input into words (words are separated by spaces)
    words = action.split()
    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]
        # the verb is: go
        if (verb == "go"):
            # set a default response
            response = "Invalid exit."
            # check for valid exits in the current room
            
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if (noun == currentRoom.exits[i]):
                    # If the exit called is door and the user hasn't solved the puzzle, don't change the room.
                    # This also calls the door() function for the puzzle to be attempted.
                    if (currentRoom.exits[i] == 'door' and door() == False):
                        break
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]
                    # set the response (success)
                    response = "Room changed."
                    # no need to check any more exits
                    break
                
            

# the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "I don't see that item."
            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if (noun == currentRoom.items[i]):
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]
                    # No need to check any more items
                    break
            # Check for valid items in the inventory
            for j in range(len(inventory)):
                # A valid item is found
                if (noun == inventory[j]):
                    # set the response to the inventory item's description
                    response = inventoryDesc[j]
                    # No need to check any more items
                    break
            # Check for valid grabbable items in the current room
            for k in range(len(currentRoom.grabbables)):
                # A valid item is found
                if (noun == currentRoom.grabbables[k]):
                    # set the response to the grabbable item's description
                    response = currentRoom.grabbablesDescriptions[k]
                    # no need to check any more items
                    break

        # the verb is: take
        elif (verb == "take"):
            # set a default response
            response = "I don't see that item."
            # Modified loop. Check for valid grabbable items in the current room
            #   - Changed the loop to be able to add grabbables' names and descriptions by using
            #       range() as opposed to the default loop counting parameter
            #   - added inventory descriptions to include grabbables' descriptions
            for i in range(len(currentRoom.grabbables)):                        
                # a valid grabbable item is found
                if (noun == currentRoom.grabbables[i]):
                    # Add the grabbable item's name to the inventory
                    inventory.append(currentRoom.grabbables[i])
                    # Add the grabbable item's description to the inventory
                    inventoryDesc.append(currentRoom.grabbablesDescriptions[i])
                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(currentRoom.grabbables[i])
                    # set the response (success)
                    response = "Item grabbed."
                    # no need to check any more grabbable items
                    break
    # display the response
    print("\n{}".format(response))
