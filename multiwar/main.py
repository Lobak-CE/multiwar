import time
from classdata import Team, print_sleep, start_a_war 
from console import setting, setting_enermydata, print_enermydata, action, print_enermyaction, choose_enermy, check_enermylife



if __name__ == "__main__": #模组化，程式多的时候可以定先后运作次序
    #游戏介绍，设定敌人队伍数量
    enermyarray = []
    origin_enermyarray = len(enermyarray)


    #设定我队的农民和军人比例
    farmer,army = setting('A')
    yourteam = Team(0,2,100,100,farmer,army,)
    yourteamarray = [yourteam]


    #显示我和敌人的数据
    print_sleep(f'\nYour data:{yourteam}\n',3)
    print_enermydata(enermyarray)  

    while True: 
        #选择你和敌人的行动，并执行
        youraction = action(yourteam)
        print_sleep(f'\nYour action is {youraction[1]}\n',3)
        print_enermyaction(enermyarray,yourteamarray)


        #你发动战争后进入的运算
        if youraction[1] == 'Start a war':
            start_a_war(yourteam, choose_enermy(enermyarray, origin_enermyarray))


        #显示你和敌人在行动后的最新数据
        print_sleep(f'\nYour data:\n{yourteam}\n')
        print_enermydata(enermyarray) 


        #检查敌人是否死亡，死亡会被移除
        check_enermylife(enermyarray)


        #判断输赢
        if yourteam.life <= 0:
            print("\nYou lose the game!")
            break
        elif len(enermyarray) == 0:
            print("\nYou win the game!")
            break

        
