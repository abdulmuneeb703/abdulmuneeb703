#ABDUL MUNEEB SYED
#9/11/2022
import globalvars
import time
def chapter4():
    print("Chapter 4")
    time.sleep(2)
    print("As he makes his way back home,he learns that the maid who had been taking care of him has been taken hostage \nby the enemies who long ago stole the kingdom and that they are also aware of his whereabouts.")
    time.sleep(4)
    print("It's Midnight and the enemies are sleeping. Take advantage of it and do not let them to see the sunrise")
    time.sleep(3)
    print("Tip: To make things back to normal, Kill the monster")
    time.sleep(3)
    R = ""
    while R != "Yes" and R !="No":
        R=input("Warriors! Are you ready to take our kingdom back? ").capitalize()
    if R=="Yes":
        print("Go ahead and Grab your Swords and horses")
        globalvars.Grabweapons = input("Choose your weapons, Sword or Arrows? ").capitalize()

    elif R=="No": #CAUSES AN ERROR, BECAUSE GLOBALVARS.GRABWEAPONS IS NOT UPDATED HERE
        print("Motivate your army and prepare for attack")
        print("Do you not want to live peacefully? yes right? then lets make it happen! Go!")

    print("Command your army to attack with", globalvars.Grabweapons, "wisely")
    import chapter5
    chapter5.chapter5()
#chapter4() use this function call to run chapter individually