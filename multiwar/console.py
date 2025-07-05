from classdata import Team, ActionMenu  
import random
import time
import sys

def check_input(question:str,condition):
    while True:   #True的情况会一直运行，理论上是无限循环，直到出现return
        try:
            value = int(input(question))
            if condition(value):   #value符合condition，而不是value等于condition；符合的话，为True
                return value
            elif value == 0:
                sys.exit() 
            else:
                print('your selection is wrong')
        except ValueError:
            print('Invalid input, input with integer')

def setting_teamnum():
    print('Welcome to the game, please set your team')
    time.sleep(1)   
    print('You can quit the game anytime by input 0')
    time.sleep(1)
    number = check_input('How many teams do you want to play?\n', lambda x: x>=1)
    return number

def setting_enermydata(enermyarray):
    number = setting_teamnum() #这里的number是console.py的函数setting_teamnum的返回值
    for i in range(number):
        farmer, army = setting('B') #这里的farmer和army是console.py的函数setting的返回值
        enermyarray.append(Team(i+1,2,100,100,farmer,army))
    time.sleep(1)


def setting(x) -> tuple[int,int]:   #箭头是为了方便我们记得return的值的种类
    if x == 'A':
        print('You can have 8 farmers and 8 armies in total')
        time.sleep(1) 
        selectmode = check_input('Select your setting mode\n1:Self\n2:Random\n', lambda x: 0<x<3)
        time.sleep(0.5) 
        if selectmode == 1:
            farmer = check_input('How much is your farmer\n', lambda x: 0<x<8)   #lambda是小function
            army = check_input('How much is your army?\n', lambda x: x == 8-farmer)
            return farmer, army     
    farmer = random.randint(1, 7)
    army = 8 - farmer
    return farmer, army


def print_enermydata(enermyarray):
    for enermy in (enermyarray):
        print(f'Enermy data:{enermy}')
        time.sleep(0.5)


def action(act,cond=None) -> int:
    actionmenu = ActionMenu(act)
    if cond==None:
        action = check_input('\nSelect your action\n1:Make Money\n2:Tranning\n3:Start a war\n',lambda x: 1<=x<=3)
    else :
        action = random.randint(1, 3)
    return actionmenu.actionfunction(action)

def enermyaction(enermyarray):
    for enermy in enermyarray:
        enermyaction = action(enermy,"") 
        return enermyaction[1]

def print_enermyaction(enermyarray):
    enermyact = enermyaction(enermyarray)
    for enermy in enermyarray:
        print(f'Enermy{enermy.id} action is {enermyact[1]}') 
        time.sleep(0.5)