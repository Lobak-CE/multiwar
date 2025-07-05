import random
import time
from classdata import Team, start_a_war 
from console import setting, setting_enermydata, print_enermydata, action, print_enermyaction, choose_enermy, check_enermylife



#run
if __name__ == "__main__": #模组化，程式多的时候可以定先后运作次序
    enermyarray = []
    setting_enermydata(enermyarray)
    origin_enermyarray = len(enermyarray)

    farmer,army = setting('A')
    yourteam = Team(0,100,100,100000,farmer,army,)

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

        if youraction[1] == 'Start a war':
            print('You start a war!')
            start_a_war(yourteam, choose_enermy(enermyarray, origin_enermyarray))

        print(f'\nYour data:\n{yourteam}\n')
        time.sleep(1)
        print_enermydata(enermyarray) 

        check_enermylife(enermyarray)

        if yourteam.life <= 0:
            print("You lose the game!")
            break
        elif len(enermyarray) == 0:
            print("You win the game!")
            break

        
