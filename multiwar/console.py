from classdata import Team, ActionMenu, start_a_war  
import random
import time
import sys

#判断玩家输入的指令是否符合要求
def check_input(question:str,condition):
   #True的情况会一直运行，理论上是无限循环，直到出现return 
    while True:   
        try:
            value = int(input(question))

            #value符合condition，而不是value等于condition；符合的话，为True
            if condition(value):   
                return value
            elif value == 0:
                print('You quit the game')
                sys.exit() 
            else:
                print('your selection is wrong')

        except ValueError:
            print('Invalid input, input with integer')


#设定敌人队伍的数量
def setting_teamnum():
    print('Welcome to the game, please set your team')
    time.sleep(0.5)   
    print('You can quit the game anytime by input 0')
    time.sleep(0.5)
    number = check_input('How many teams do you want to play?\n', lambda x: x>=1)
    return number


#设定敌人队伍的农民和军队比例
def setting_enermydata(enermyarray):
    #这里的number是console.py的函数setting_teamnum的返回值
    number = setting_teamnum() 

    #这里的farmer和army是console.py的函数setting的返回值
    for i in range(number):
        farmer, army = setting('B') 
        enermyarray.append(Team(i+1,2,100,100,farmer,army))
    time.sleep(0.5)


#设定农民和军队比例的逻辑
def setting(x) -> tuple[int,int]:   
    if x == 'A':
        print('You can have 8 farmers and 8 armies in total')
        time.sleep(0.5) 
        selectmode = check_input('Select your setting mode\n1:Self\n2:Random\n', lambda x: 0<x<3)
        time.sleep(0.5) 
        if selectmode == 1:
            farmer = check_input('How much is your farmer\n', lambda x: 0<x<8)  
            army = check_input('How much is your army?\n', lambda x: x == 8-farmer)
            return farmer, army     
    farmer = random.randint(1, 7)
    army = 8 - farmer
    return farmer, army


#显示敌人的数据
def print_enermydata(enermyarray):
    for enermy in (enermyarray):
        print(f'Enermy data:{enermy}')
        time.sleep(0.5)


#传达给classdata敌我行动的种类
def action(act,cond=None) -> int:
    actionmenu = ActionMenu(act)
    if cond==None:
        action = check_input('\nSelect your action\n1:Make Money\n2:Tranning\n3:Start a war\n',lambda x: 1<=x<=3)
    else :
        action = random.randint(1, 3)
    return actionmenu.actionfunction(action)


#显示敌人的行动，如果打战就传达给classdata谁发动战争
def print_enermyaction(enermyarray,yourteamarray):
    enermyactarray = []

    for enermy in enermyarray:
        enermyaction = action(enermy,'')
        enermyactarray.append(enermyaction[1])
        print(f'Enermy{enermy.id} action is {enermyaction[1]}') 
        time.sleep(0.5)

    for index, enermy in enumerate(enermyactarray):
        if enermy == 'Start a war':
            time.sleep(0.5)
            print(f'\nEnermy{enermyarray[index].id} starts a war!')
            filter_enermy = [i for i in enermyarray if i != enermyarray[index]]
            combinedlist = filter_enermy + yourteamarray
            start_a_war(enermyarray[index],random.choice(combinedlist))
            time.sleep(0.5)


#玩家发动战争，选择对哪一个敌人进攻
def choose_enermy(enermyarray,origin_enermyarray):
    while True:
        enermyid = check_input('\nSelect your enermy with id:', lambda x: 0<x<=origin_enermyarray)
        for enermy in enermyarray:
            if enermyid == enermy.id:
                print(f'You choose enermy{enermy.id}')
                return enermy
        print(f'Enermy{enermyid} is dead! Select another enermy')


#检查敌人是否死亡，死亡会被移除
def check_enermylife(enermyarray):
    for enermy in enermyarray:
        if enermy.life <= 0:
            time.sleep(0.5)
            print(f'Enermy{enermy.id} is dead')
            time.sleep(0.5)
            enermyarray.remove(enermy)
