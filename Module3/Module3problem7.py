#ABDUL MUNEEB SYED
#7/22/2022
#problem7
#This program will calculate the length of the Holiday by taking the input from the users
#From 0-6 select a day where 0 is Sunday and 6 is Saturday
Start_Day= int(input("Vacation Start Day (From 0-6): "))
Period = int(input("Length of your Holiday: "))
LastVacation_day= (Start_Day + Period) % 7
print("Your back to home by", LastVacation_day)

