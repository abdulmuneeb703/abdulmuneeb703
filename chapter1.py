#ABDUL MUNEEB SYED
#9/11/2022
import time
import globalvars #imports all global variables, must be referenced with globalvars.[variable name]
def chapter1():
    globalvars.init() #Initializes all variables-- make sure this only runs in chapter 1!
    print("Prince", globalvars.Username) #prints the initial value of Username, "Abdul"
    print("Welcome to the Adventure Game")
    time.sleep(2) #Pauses the game for exactly 3 seconds.
    globalvars.Username=input("What's your name? ")
    print("Prince", globalvars.Username) #updates the value of Username, this will be tracked across all modules
    time.sleep(3)
    print("You are the prince and now you are ready to begin the Adventure")
    time.sleep(3)
    print("The prince had a choice between training Horse riding and training his Sword fighting")
    time.sleep(3)
    skillchoice1 = input("Select A to ride a Horse, or B to train for Sword fighting ")

    if skillchoice1 =="A":
        print("The prince decided to train for Horse Riding")
    elif skillchoice1 == "B":
        print("The prince has decided to train for Swordfighting ")


    globalvars.Horseriding +=1 #Horseriding's value is now 1, this is tracked across all modules
    print("Hurray! You made it! You are now prepared to enter the next Chapter")
    import chapter2
    chapter2.chapter2()

#chapter1()  Use this function call if running the chapter1 individually
