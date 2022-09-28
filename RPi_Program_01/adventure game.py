#The adventure game code
import random
import sys
import time

a= 2
b=0.2
c=0.08


def intro():
    print()
    print("(Everything is Dark)")
    print("You feel around, using your hands to see , which is probably not a good idea")
    print("The ground is cold,wet,and not to mention your hungry")
    print(" You feel something that seems like a rock it sinks into the ground")
    print("You begin to see a bright light ")
    print("You think to yourself (is this my time)")
    print()
    print("It's a cave..!!!?")
    print()
    print("The rock moved a boulder that was blocking an entrance")
    print("Three paths are revealed:")
    print("Path #1: Move foward through the caves entrance, into the light.")
    print("Path #2: A side entrance that looks like it leads to a room that seems to be playing music")
    print("Path #3: Climb back down the vines where you came from")
    print()
    firstPath = input("Which path will you choose?  (1/2/3):")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()


def path1():
    print()
    print("You walk into the room of oplympus")
    print("You see Zeus,Athena,Hercules,etc")
    print("There all sitting at the table monitoring chronos and hades ")
    choose=input("Who will you talk to (Zeus/Athena/Hercules)")
    if choose=='zeus' or choose=='Zeus':
        print()
        zeus()
    elif choose=='Hercules' or choose=='hercules':
        print()
        hercules()
    elif choose=='Athena' or choose=='athena':
        print()
        athena()
        

def zeus():
    print()
    print("...Mortal what will we have done should you deal with Hades or Chronos")
    print("...Hermes can transport you to whichever realm...")
    transport=input("Go to Chronos or Go to Hades (Hades/Chronos)")
    if transport=='Chronos' or transport=='chronos':
        print()
        chronosStart()
    elif transport=='Hades' or transport=='hades':
        print()
        hadesStart()

def hercules():
    print()
    print("...Hades is an evil like no other who is choosing to wipe out all the realms...")
    print("...You must defeat Hades...")
    print("Hercules picks you up and sends you to the under world")
    time.sleep(c)
    hadesStart()
def athena():
    print()
    print("...Chronos is plotting something and is equally as dangerous and has the power to stop time as we know it...")
    print("...Chronos has alwas been a threat to our way of life..")
    print("...Stop him...")
    print("... I will send you to his realm...")
    time.sleep(c)
    chronosStart()

def path2():
    print()
    print("You walk into the room and to your suprise it's a big party")
    print("Gods from every pantheon is there")
    print("It seems like a good time Hermes is standing behind you telling you to converse")

    

def path2_1():
    print()

def path2_2():
    print()
def path2_3():
    print()


def path3():
    print("You climb down the vines into a bottomless hole into the ground" )
    print("It seems to be the entrance to something")
    print("##########################")
    print("#####   HADES ############")
    print("##########################")
    print("Someone called out to you")
    print()
    print(' "Hey, strange traveller.."')
    print("....My name is Hermes... God of Swiftness I'll be your ticket out of here...")
    print("...Everyone here knows who you are. Your looking to defeat father time right?...")
    print("...Well whatver your here for your in the wrong domain kid...")
    print("...This is where the King of Despair lives Hades...")
    print("...Chronos is just below here and He will test your might if you meet him...")
    print("Hermes wil transport you anywhere on Mount Olympus")
    print("Path #1: Hermes will take you back up into the cave into the cave entrance.")
    print("Path #2: You can stay in Hades and look around for this King of despair.")
    print("Path #3: Descend down to meet Chronos.")
    print()
    secondPath = input("Which path will you choose? (1/2/3)")
    if secondPath == '1':
        print()
        path1_1()
    elif secondPath == '2':
        print()
        hadesStart()
    elif secondPath == '3':
        print()
        chronosStart()
    
def hadesStart():
    print()
    print("You look around the eerie place")
    print("The rivers have fire and there are souls ,moaning and crying to be released it smells like death")
    print("Almost on time Hades appears with his long black robe and hair like crimson")
    print()
    print("...You dare enter my realm what are you a fool...")
    print("...I am the King of Despair...")
    print("...I will swallow your soul and reclaim olympus and this world...")
    print("This was the true evil he only here for one thing to end life as we know it")
    print("He must be defeated")
    hades=input("Will you defeat Hades? (y/n)")
    if hades=='y' or hades=='Y':
        print()
        hadesEnd()
    elif hades=='n' or hades=='N':
        print()
        print("You lose everything")
        playagain()
def hadesEnd():
    print("##################")
    print("### ENTER HADES###")
    print("##################")
    print()
    print("the fight begins Hades hurls a fiery rock at you")
    quicktime=input("Dodge left or right")
    if quicktime=="left" or quicktime=="Left":
        print()
        hermesEvent()
    elif quicktime=='right' or quicktime=='Right':
        print("You died try again")
        time.sleep(b)
        hadesEnd()

def hermesEvent():
    print("You dodge left and he picks up the spear of faith in order to judge your soul")
    print("There's nothing you can do but have a battle of will")
    print("You must exhibit the strength of humanity you slay hades with your overwhelming might")
    print("You won it's over his reign of terror has passed")
    print("Hermes comes down from the heavens")
    print("...Good job hades is dead and chronos is pleased he has decided to chill out for once in his life...")
    print("...Would you like to go home or go with me...")
    hermes=input("Follow Hermes (y/n)")
    if hermes=='y' or hermes=='Y':
        print()
        path2()
    elif hermes=='n' or hermes=='N':
        print("Rest easy warrior")
        time.sleep(b)
        playagain()
    
    
def chronosStart():
    print()
    print("You went down into the lair of chronos")
    print("It was big but small at the same time as if the reality was being warped")
    print("You were in a Galaxy in a limitless plane of existence")
    print("You see a book thats labled Secrets of Time encapsulated in the beam of light, also Chronos is standing to the side challenging you")
    print()
    print("Should you steal the book and understand the laws of time and reality itself or Fight Chronos to end his terror")
    thirdPath=input("What wil you do become a Hero or a God? (Steal the book/Fight Chronos)")
    if thirdPath=='Steal the Book' or thirdPath=='Steal the book':
          print()
          bookEnd()
    elif thirdPath=='Fight Chronos' or thirdPath=='Fight chronos' :
        print()
        chronosEnd()
def bookEnd():
    print("You steal the book of time")
    print("Chronos stands in awe as you begin to become a time gode as well")
    print("You begin to realize the gravity of the situation")
    print("...Chronos screams out you fool what have you done...")
    print("...There can only be one time god...")
    print("...You must reset the timeline defeat me another way there must be balance...")
    godPath=input("Will you remain a time god (Y/N) ?")
    if godPath=='Yes' or godPath=='y':
        print()
        print("This is your life now forced to hold reality in your hand trapped in this lair")
        playagain()
    elif godPath=='No' or godPath=='n':
        print()
        print("You begin to reset the timeline to the very beginning of your adventure")
        print()
        intro()



def chronosEnd():
    print("Chronos stands up the reailty is being bent around him as he walks")
    print("#############################")
    print("### Enter Chronos ###########")
    print("#############################")
    print("When Chronos talked it almost was earth shattering as if time itself had no effect on his words")
    time.sleep(c)
    print("...You dare challeneg me boy...")
    print("... A mere mortal who stands in the way to defy the Gods...")
    print("..How about this we will play one your mortal games...")
    print("... I fancy myself a godly gambler..")
    print("gambling you thought the father of time wants to let this be decided by a gambling game")
    print("... Yesssss here is the game gues the number and im feelin generous you get four attempts to win..")
    print("..I'm thinking of a number from 1 to 10 either guess it or pay the consequences...")
    print("...Now prepare yourself silly mortal..")
    fourthPath=input("Save the World and Yourself!")
    if fourthPath=='Ok' or fourthPath=='Yea' or fourthPath=="Lets's go" or fourthPath=='ok':
        print()
        game()
    



def game():
    num = random.randint(1, 10)
    print(f'''
----------------------------------
Battle of Life and Death: Ragnorak
----------------------------------
''')
    attempt = 4
    msg = 'You Lost Now Die'
    while attempt > 0:
        user_input = int(input('Enter Number: '))
        if user_input == num:
            print("...You Won..")
            msg = endGame()
            break
        elif user_input > num:
            print(f'{user_input} is greater.\nRemaining attempts: {attempt}.')
            attempt -= 1
        elif user_input < num:
            print(f'{user_input} is smaller.\nRemaining attempts: {attempt}.')
            attempt -= 1
        else:
            print("Thats not a number stupid human")
            break
    print(msg)


def endGame():
    print()
    print("The world begans to crumble around and glass starts to shatter as the realm of Chronos is fallen")
    print(" As Chronos is dying he begins to mumble")
    print("...Silly mortal the cycle never ends..")
    print("...Enjoy this victory for soon this world will dive into despair..")
    print(" ... I was never the real enemy...")
    print("Adventure is Done")
    playagain()
    
   
def playagain():
    endgame1=input("Would you like to play again (Y/N)")
    if endgame1=='Y' or endgame1=='y':
        time.sleep(b)
        start()
    elif endgame1=='N' or endgame1=='n':
        print()
        print("Roll the credits")
    
        
        
    




def start():
    print()
    print()
    print("   ###########################")
    print("   #                         #")
    print("   #   The Time Anomally     #")
    print("   #                         #")
    print("   ###########################")
    print()
    print()
    print()
    print("Que Que.. WHat happened? ")
    print("It's pitch black I can't see jack or jill haha still got jokes")
    print()
    startGame = input("Would you like to start the game? (Y/N): ")
    if startGame == 'n' or startGame == 'N':
        print("what are you scared, Get back in the Adventure?")
    elif startGame == 'y' or startGame == 'Y':
        intro()
start()


