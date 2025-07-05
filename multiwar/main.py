import random
import time
from classdata import Team#, start_a_war  
from console import setting, setting_enermydata, print_enermydata, action, print_enermyaction



#run
if __name__ == "__main__": #模组化，程式多的时候可以定先后运作次序
    enermyarray = []
    setting_enermydata(enermyarray)

    farmer,army = setting('A')
    yourteam = Team(0,2,100,100,farmer,army,)

    time.sleep(0.5)
    print(f'\nYour data:{yourteam}\n')
    time.sleep(1)
    print_enermydata(enermyarray)  

    while True:  #无限循环，直到break
        youraction = action(yourteam)
        time.sleep(1)
        print(f'\nYour action is {youraction[1]}\n')  
        time.sleep(1)
        print_enermyaction(enermyarray)

        # if youraction[1] == 'Start a war' or enermyaction[1] == 'Start a war':
        #     start_a_war(yourteam, teamB)
        print(f'\nYour data:\n{yourteam}\n')
        time.sleep(1)
        print_enermydata(enermyarray) 

        # if yourteam.life <= 0 or teamB.life <= 0:
        #     if yourteam.life <= 0:
        #         print("You lost the game!")
        #     else:
        #         print("You won the game!")
        #     break

        # if yourteam.life <= 0:
        #     print("You lost the game!")
        # elif Team.number == 1:
        #     print("You won the game!")
        # break

        
