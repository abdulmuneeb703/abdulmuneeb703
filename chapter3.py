#ABDUL MUNEEB SYED
#9/11/2022
import time
import globalvars
def chapter3():
    print("Chapter 3")
    print("To become a warrior, you need to learn more about the skills and wisedom")
    time.sleep(2)
    Q= input("Do you want to learn more? Yes or No  ").capitalize()
    #Q = Q.capitalize()
    if Q == 'Yes':
            print(Q)
    else:
        print("You have no other choice")
        time.sleep(3)
    print("Meet the wise man sitting under the shade of tree")
    time.sleep(3)
    skill= input("What skills do you want to specialize in? Enter H for Horse riding and S for Swordfighting").upper()
    #skill = skill.upper()
    print(skill)
    import chapter4

    while skill != 'H' and skill != 'S': #continuously prompts the user as long as the answer they give is neither H nor S
        skill = input("Please enter either H or S.").upper()
        #skill = skill.upper()
    if skill =='H':
        print("Great choice! You are now a pro rider!")
        globalvars.Horseriding += 1
    elif skill =="S":
        print("Great! You're a warrior")
        globalvars.Swordfighting += 1
    print("You are now ready to conquere your kingdom back, All the best")
    chapter4.chapter4()
#chapter3() use this function call to run chapter individually