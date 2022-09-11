#ABDUL MUNEEB SYED
#9/11/2022
import time
import globalvars #imports everything from globalvars
#from globalvars import Horseriding as horseskill #Imports ONLY Horseriding from globalvars, and gives it the alias 'horseskill'
#print(horseskill)
def chapter2():
    print("The enemy soldiers are chasing you")
    time.sleep(3)
    print("Horseriding skill is:", globalvars.Horseriding)

    import chapter3 #Makes sure that we have access to chapter3.chapter3()
    if globalvars.Horseriding==1:
        print("You escape them easily on Horseback!")
        chapter3.chapter3() #moves to chapter 3 if we win

    elif globalvars.Swordfighting == 1:
        print("Great! You've smashed them!")
        chapter3.chapter3()

    else:
        print("You are trapped")
        print("GAME OVER :(")
        import chapter1
#chapter2() use this function call to run chapter individually

