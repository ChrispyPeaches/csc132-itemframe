###########################################################################
# Name:         Chris Perry, Sharantz Green, Lucas Alvarado, Cory Strickland
# Date:         10/5/22
# Description:  A text-based game that puts a user in a mansion with 4 rooms.
############################################################################
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
#                           -Before you meet your demise,prove your worth
#                           -there is a battle room that allow you to "fight" the cpu
#                           - When they loose the game, a skull displays.
#
######################################################################
######################################################################
from random import randint
from time import sleep
import random
from tkinter import *
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

#####################
## ADDED FUNCTIONS ##
#####################

# the blueprint for a room


class Room:
    # the constructor
    def __init__(self, name, image):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.image = image
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
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

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
        # Adds descriptions to grabbable items
        self._grabbablesDescriptions.append(desc)

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


# the game class
# inherits from the Frame class of Tkinter
class Game(Frame):
    # the constructor
    def __init__(self, parent):
        # call the constructor in the superclass
        Frame.__init__(self, parent)
        # Set the passphrase for the puzzle
        self.passphrase = "Puzzle Passphrase"
        # Encodes the given phrase for the puzzle and stores it
        self.encodedPhrase = self.doorPuzzleEncode()
        # Keeps track of how many times the user accessed the door function
        self.doorAttempts = 0
        # Keeps track of it the user succeeded the door puzzle
        self.doorSuccess = False

    # Plays the game

    def play(self):
        # add the rooms to the game
        self.createRooms()
        # nothing in inventory...yet
        self.inventory = []
        # Adds a container to store descriptions of items and grabbables in the inventory
        self.inventoryDesc = []
        # Initialized and configure the GUI
        self.setupGUI()

    # Creates the rooms
    def createRooms(self):
        # self.r1 through self.r4 are the four rooms in the mansion
        # currentRoom is the room the player is currently in (which can
        # be one of self.r1 through self.r4)
        # since it needs to be changed in the main part of the program,
        # it must be global
        # create the rooms and give them meaningful names and images to match
        self.r1 = Room("Room 1", "resources/room1full.png")
        self.r2 = Room("Room 2", "resources/room2dog.png")
        self.r3 = Room("Room 3", "resources/room3full.png")
        self.r4 = Room("Room 4", "resources/room4full.png")
        # Adds a room where if the user is here, they've won the game
        self.r5 = Room("Outside", "resources/win.png")
        #Adds a battle room part of the battle done for gui
        self.r6 = Room("Battle", "resources/battle.png")
        #Adds a room where if the user dies it displays a death message
        self.r7 = Room("Death", "resources/dead.png") 
        # Adds a "room" for the door puzzle. Done for GUI purposes, from an abstract POV, this is not a room
        self.r8 = Room("Door", "resources/thedoor.png")

        ############
        ## ROOM 1 ##
        ############
        # add exits to room 1
        self.r1.addExit("east", self.r2)  # -> to the east of room 1 is room 2
        self.r1.addExit("south", self.r3)
        self.r1.addExit("door", self.r5)
        # add grabbables to room 1
        self.r1.addGrabbable(
            "key", "A golden key. Doesn't look like it'll decipher anything.")
        # add items to room 1
        self.r1.addItem(
            "chair", "It is made of wicker and no one is sitting on it.")
        self.r1.addItem(
            "table", "It is made of oak. A golden key rests on it.")

        ############
        ## ROOM 2 ##
        ############
        # add exits to room 2
        self.r2.addExit("west", self.r1)
        self.r2.addExit("south", self.r4)
        # add items to room 2
        self.r2.addItem(
            "rug", "It is nice and Indian. It also needs to be vacuumed.")
        self.r2.addItem("fireplace", "It is full of ashes.")
        self.r2.addItem(
            "dog", "It looks back at you, perhaps inviting you to pet it?")

        ############
        ## ROOM 3 ##
        ############
        # add exits to room 3
        self.r3.addExit("north", self.r1)
        self.r3.addExit("east", self.r4)
        # add grabbables to room 3
        self.r3.addGrabbable(
            "book", "It's a book of ciphers. Chapters: Caesar, Vigenère, Pigpen, and Playfair")
        # add items to room 3
        self.r3.addItem("bookshelves", "They are empty. Go figure.")
        self.r3.addItem("statue", "There is nothing special about it.")
        self.r3.addItem("desk", "The statue is resting on it. So is a book.")

        ############
        ## ROOM 4 ##
        ############
        # add exits to room 4
        self.r4.addExit("north", self.r2)
        self.r4.addExit("west", self.r3)
        self.r4.addExit("south", self.r6)  # DEATH!
        # add grabbables to room 4
        self.r4.addGrabbable(
            "6-pack", "It read's the brand 'Jrbiibo'p'. You recognize the graphics to be the 'Mueller's' Brand")
        # add items to room 4
        self.r4.addItem(
            "brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")
        # set room 1 as the current room at the beginning of the game
        self.currentRoom = self.r1
        ################
        # Room 6 #####
        ###########

    def battle(self):
        # The user is giving a limited amount of attempts to guess the number the computer is thinking
        # It prompt you to enter the number then tells whether you are higher or lower than the number
        # If you lose you get sent to death room otherwise your sent to the winning room
        # Bind the return key to the processing of input for the door puzzle
        self.player_input.bind("<Return>", self.battleProcessInput)
        self.player_input.delete(first=0, last=END)
        self.text.config(state=NORMAL)
        #This where the random number is generated and the text that is displayed in the gui
        self.generatednum = random.randint(1, 10)  # change vak to 10
        self.attempt = 4
        self.text.insert(END, "You jumped out of a window\n")
        self.text.insert(END, "You get a second chance at life.\n")
        self.text.insert(END, ("Enter Number: \n"))

    def battleProcessInput(self, event):
        # prompt for player input
        # waits to read the number 
        # if you lose your sent to the death room
        self.text.config(state=NORMAL)
        self.text.delete("1.0", END)
        # This is actualy lines of code for the battle game againt the cpu
        if (isinstance(self.player_input.text, int) == False):
            return None
        user_input = int(self.player_input.get())
        self.player_input.delete(first=0, last=END)
        if self.attempt > 0:
            if (user_input == self.generatednum):
                self.currentRoom = self.r5
            elif user_input > self.generatednum:
                self.attempt -= 1
                self.text.insert(
                    END, f"{user_input} is greater.\nRemaining attempts: {self.attempt}.\n")
            elif user_input < self.generatednum:
                self.attempt -= 1
                self.text.insert(
                    END, f"{user_input} is smaller.\nRemaining attempts: {self.attempt}.\n")
            #logic for updating the status post figuring out the number whether you win or lose
        self.text.config(state=DISABLED)
        if (user_input == self.generatednum):
            self.updateStatus()
        else:
            self.text.insert(END, "Try AGAIN\n")
        if (self.attempt == 0):
            self.currentRoom = self.r7
            self.updateStatus()

    # sets up the GUI
    def setupGUI(self):
        # Organize the GUI.
        self.pack(fill=BOTH, expand=1)

        # The widget is a Tkinter Entry.
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        self.player_input = Entry(self, bg="white")
        self.player_input.bind("<Return>", self.processInput)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        self.text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        self.text = Text(self.text_frame, bg="lightgrey", state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        self.text_frame.pack(side=RIGHT, fill=Y)
        self.text_frame.pack_propagate(False)

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        self.image = Label(self, width=WIDTH // 2, image=img)
        self.image.image = img
        self.image.pack(side=LEFT, fill=Y)
        self.image.pack_propagate(False)

        self.updateStatus()

    # sets the current room image
    def setRoomImage(self):
        if (self.currentRoom == "Death"):
            self.img = PhotoImage(file="resources/dead.png")
        elif (self.currentRoom == "Battle"):
            self.img = PhotoImage(file="resources/battle.png")
        #sets the room image to show no items
        elif ("key" not in self.r1.grabbables and self.currentRoom is self.r1):
            self.img = PhotoImage(file="resources/room1.png")
        elif ("dog" not in self.r2.items and self.currentRoom is self.r2):
            self.img = PhotoImage(file="resources/room2.png")
        elif ("book" not in self.r3.grabbables and self.currentRoom is self.r3):
            self.img = PhotoImage(file="resources/room3.png")
        elif ("6-pack" not in self.r4.grabbables and self.currentRoom is self.r4):
            self.img = PhotoImage(file="resources/room4.png")
        else:
            self.img = PhotoImage(file=self.currentRoom.image)
        self.image.config(image=self.img)
        self.image.image = self.img

    # sets the status displayed on the right of the GUI
    def updateStatus(self, response=""):
        # display the status
        self.text.config(state=NORMAL)
        self.text.delete("1.0", END)
        if (self.currentRoom.name == "Battle"):
            self.battle()
            self.setRoomImage()
        elif (self.currentRoom.name == "Death"):
            # if dead, let the player know and disable player input
            self.player_input.config(state=DISABLED)
            self.text.insert(
                END, "You are dead. The only thing you can do now is quit.\n")
            self.setRoomImage()
            self.text.config(state=DISABLED)

        elif (self.currentRoom.name == "Outside"):
            # if player won, let the player know and disbale player input
            self.player_input.config(state=DISABLED)
            self.text.insert(
                END, "Congrataz! You won!\n")
            self.setRoomImage()
            self.text.config(state=DISABLED)

        else:
            # set the status so the player has situational awareness
            # the status has room and inventory information
            self.status = f"{self.currentRoom}\nYou are carrying: {self.inventory}\n"
            # otherwise, display the appropriate status
            self.text.insert(END, str(f"{self.status}\n\n{response}"))
            self.setRoomImage()
            self.text.config(state=DISABLED)

    # Processes input from the entry input from the GUI
    def processInput(self, event):
        # prompt for player input
        # the game supports a simple language of <verb> <noun>
        # valid verbs are go, look, and take
        # valid nouns depend on the verb
        # set the user's input to lowercase to make it easier to compare
        # the verb and noun to known values
        action = self.player_input.get().lower()
        # exit the program if the player wants to leave (supports quit,
        # exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye"):
            endgame()
        # split the user input into words (words are separated by spaces)
        words = action.split()
        response = ""
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
                for i in range(len(self.currentRoom.exits)):
                    # a valid exit is found
                    if (noun == self.currentRoom.exits[i]):
                        # If the door exit is called, lead the user to the door puzzle.
                        # "return None" is here so when waiting for input for the door puzzle,
                        # the rest of the code in this function doesn't run.
                        if (self.currentRoom.exits[i] == 'door'):
                            self.doorPuzzlePlay()
                            return None
                        # change the current room to the one that is
                        # associated with the specified exit
                        self.currentRoom = self.currentRoom.exitLocations[i]
                        # set the response (success)
                        response = "Room changed."
                        # no need to check any more exits
                        break
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."
                # check for valid items in the current room
                for i in range(len(self.currentRoom.items)):
                    # a valid item is found
                    if (noun == self.currentRoom.items[i]):
                        # set the response to the item's description
                        response = self.currentRoom.itemDescriptions[i]
                        # No need to check any more items
                        break
                # Check for valid items in the inventory
                for j in range(len(self.inventory)):
                    # A valid item is found
                    if (noun == self.inventory[j]):
                        # set the response to the inventory item's description
                        response = self.inventoryDesc[j]
                        # No need to check any more items
                        break
                # Check for valid grabbable items in the current room
                for k in range(len(self.currentRoom.grabbables)):
                    # A valid item is found
                    if (noun == self.currentRoom.grabbables[k]):
                        # set the response to the grabbable item's description
                        response = self.currentRoom.grabbablesDescriptions[k]
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
                for i in range(len(self.currentRoom.grabbables)):
                    # a valid grabbable item is found
                    if (noun == self.currentRoom.grabbables[i]):
                        # Add the grabbable item's name to the inventory
                        self.inventory.append(self.currentRoom.grabbables[i])
                        # Add the grabbable item's description to the inventory
                        self.inventoryDesc.append(
                            self.currentRoom.grabbablesDescriptions[i])
                        # remove the grabbable item from the room
                        self.currentRoom.delGrabbable(
                            self.currentRoom.grabbables[i])
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable items
                        break

            # the verb is: pet
            elif verb == "pet":                                    
                response = "you can't pet that."         # set a default response 
                if "dog" in self.currentRoom.items:      # checks if dog is in list of room items
                    response = "You reach out to pet the dog, it leaps forward and bites you. Before you can do anything it flees out of the room."
                    self.currentRoom.items.remove("dog")    # if yes message is diplayed and dog is removed from list, set room image to remove dog 
                    self.setRoomImage()

            # the verb is drink
            elif verb == "drink":
                response = "you can't drink that."      # set a default response
                if "6-pack" in self.inventory:          # added drinking the brew, it kills you
                    response = "You drink the brew, it smells funny. You pass out for mysterious reasons and dont awaken."
                    self.currentRoom = self.r6          # sets to death room, displays death message 
            else:
                response = "I don't understand. Try verb noun.  Valid verbs are go, look, drink, pet, and take"
        else:
            # Improper command
            response = "I don't understand.  Try verb noun.  Valid verbs are go, look, drink, pet, and take"
        # display the response. Clears input box
        self.player_input.delete(first=0, last=END)
        self.updateStatus(response)

    # This function encodes the phrase for the door puzzle.
    def doorPuzzleEncode(self):
        #       - It does this by taking a list of all alphabetic characters, one for upper case, one for lower case
        #           and shifts it by a random amount with a possible range of [3,7] shifted characters, then converts
        #           the characters to a string.
        #           - To account for wrapping around from z to a in the alphabetic lists, uses the mod operator
        #               in order to find how many letters it needs to shift after wrapping around to a in the list
        #       - I also added future proofing to be able to randomize which cipher is used if more possible ciphers
        #           are added, such as the ones listed in the "book" item in one of the rooms. Any cipher used is to be
        #           added to the description of the "book" item.
        encoding = 'caesar'
        if (encoding == 'caesar'):
            inpt = self.passphrase
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            alphabetl = "abcdefghijklmnopqrstuvwxyz"

            for i in range(0, randint(3, 7)):
                output = [0 for i in range(len(inpt))]
                for j in range(0, len(inpt)):
                    for k in range(0, 26):
                        if (inpt[j] == alphabet[k]):
                            output[j] = alphabet[(k+i) % len(alphabet)]
                        elif (inpt[j] == alphabetl[k]):
                            output[j] = alphabetl[(k+i) % len(alphabet)]
                        elif inpt[j] == "'" or inpt[j] == ",":
                            output[j] = inpt[j]
                        elif inpt[j] == " ":
                            output[j] = inpt[j]
                s = ""
                for spot in output:
                    s += str(spot)
        return s

    #   This funciton starts the door puzzle where the cipher is implemented.
    def doorPuzzlePlay(self):
        #   - The user is told a phrase and is instructed to decipher the phrase. They'll be able to find
        #       a list of ciphers in the "book" item in Room 3
        #   - The door gives different responses based on success and how many times the user has accessed it
        #       the door to decrease annoyance with the puzzle
        #   - I got this idea from a D&D puzzle for my campaign I created with similar attributes
        # Bind the return key to the processing of input for the door puzzle
        self.player_input.bind("<Return>", self.doorPuzzleProcessInput)
        self.player_input.delete(first=0, last=END)
        self.text.config(state=NORMAL)
        self.text.delete("1.0", END)
        if (self.doorAttempts == 0):
            #updates image to show the door
            self.currentRoom = self.r8
            self.setRoomImage()
            self.text.insert(END, str(
                f"The Door speaks,\n'Don't be brash, solve my puzzle in order to pass.'\nDecipher this phrase.\n{self.encodedPhrase}"))
        else:
            #updates image to show the door
            self.currentRoom = self.r8
            self.setRoomImage()
            self.text.insert(
                END, str(f"The Door speaks,\nDecipher this phrase.\n{self.encodedPhrase}"))
        self.text.config(state=DISABLED)

    # Processes the input for the door puzzle
    def doorPuzzleProcessInput(self, event):
        #   - If the user puts in the correct deciphered phrase, the function sets self.doorSuccess to True, otherwise False
        #       - This tells the program whether to go to the "Outside" room, or back to the room they were in
        response = ""
        self.text.config(state=NORMAL)
        if (self.player_input.get() == self.passphrase):
            self.doorSuccess = True
        else:
            if (self.doorAttempts < 3):
                #returns to room 1 image
                self.currentRoom = self.r1
                self.setRoomImage()
                response = "\nThe Door speaks,\n'Invalid. Come back and try again. There might be a clue somewhere...'"
            else:
                #returns to room 1 image
                self.currentRoom = self.r1
                self.setRoomImage()
                response = f"\nThe Door speaks,\n'Invalid. You might wanna look for clues in {self.r3.name}'"

            self.doorAttempts += 1
            self.doorSuccess = False
        self.text.config(state=DISABLED)
        # Update variables and return to the main game
        self.doorPuzzleReturnToGame(response)

    # This prepares the user to go back to the original game
    def doorPuzzleReturnToGame(self, response=""):
        # Bind the return key back to the processing of input for the normal game
        self.player_input.bind("<Return>", self.processInput)
        self.player_input.delete(first=0, last=END)
        # Change the current room to "Outside" if the door was successfully completed.
        if self.doorSuccess == True:
            self.currentRoom = self.r5
        # Return back to the normal game.
        self.updateStatus(response)


def endgame():
    window.destroy()
    exit()


##########################################################
# START THE GAME!!!
##########################################################
# the default size of the GUI is 800x600
WIDTH = 800
HEIGHT = 600

# create the window. Set title. Set x button to stop program. Set resolution to specified values.
window = Tk()
window.title("Room Adventure")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.protocol("WM_DELETE_WINDOW", lambda: endgame())

# create the GUI as a Tkinter canvas inside the window
g = Game(window)

g.play()
# play the game

window.mainloop()
