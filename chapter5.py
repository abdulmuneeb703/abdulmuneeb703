#ABDUL MUNEEB SYED
#9/11/2022
import globalvars
def chapter5():
    print("You are now ready to invade the kingdom")
    print("Command the army to attack the kingdom from all the sides and you focus on monstor and save your maid")
    print("Take the monster down and smash him off")
    print("Run and save the maid")
    if globalvars.Swordfighting >= 1 and globalvars.Horseriding >= 1:
        print("Maid Saved. Mission Successful. Hurraayy!! :) ")
    else:
        print("You are not good enough at swordfighting and horseriding to save the maid and replay the game")
        import chapter1
        chapter1.chapter1()
#chapter5() use this function call to run chapter individually