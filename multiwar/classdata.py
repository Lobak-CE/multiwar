import random
import time



#每个队伍的参数
class Team:  
    def __init__(self, id, life, money, military, farmer, army):   #self是变量，我也可以换成其他名字，但一般都用self
        self.id = id
        self.life = life  
        self.money = money
        self.military = military
        self.farmer = farmer
        self.army = army


    #当有人call整个Team，会return这个值
    def __str__(self):   
        return f'id:{self.id}, life:{self.life}, money:{self.money}, military:{self.military}, farmer:{self.farmer}, army:{self.army}'
    
    
    #赚钱和练兵行动执行，改变队伍的参数
    def proceed(self,index):
        if index==1:
            plus = (self.farmer/3) +1
            if self.money > 0:
                self.money = round(self.money * plus,2)
            else:
                self.money += 100
            actionname = 'Make Money'
            return self.money, actionname 
        elif index==2:
            plus = (self.army/3) +1
            if self.money > 0:
                self.military = round(self.military + self.money * plus,2)
                self.money = 0
            else:
                self.military += 100
            actionname = 'Tranning'
            return self.military, actionname
        

#判断行动的编号，传达至proceed
class ActionMenu:  
    def __init__(self,act):   #这里的self是ActionMenu的变量，act是Team的变量
        self.act=act

    def actionfunction(self,index):   #当输入ActionMenu.Make_Money.actionfunction，就会返回self.make.money，执行制定的def
        if index <=2:
            return self.act.proceed(index)
        else :
            actionname = '','Start a war'
            return actionname 


def print_sleep(printtext, sequence=1, sleeptime=0.5):
    if sequence == 1:
        print(printtext)
        time.sleep(sleeptime)
    elif sequence == 2:
        time.sleep(sleeptime)
        print(printtext)
    elif sequence == 3:
        time.sleep(sleeptime)
        print(printtext)
        time.sleep(sleeptime)


#发动战争的胜负计算
def start_a_war(A,B):
    print(f'Team:{A.id} starts a war with Team:{B.id}')
    winner = random.choices([A,B],weights=[A.military,B.military],k=1)   #weight是胜负的概率   #要用choices而不是choice，因为有概率计算
    time.sleep(2)
    if winner == [A]:   #一定要[A]而不是A，因为choice的是一个list
        print_sleep(f'\nTeam:{A.id} win the war!')
        print_sleep(f'Team:{B.id} lose the war!\n')
        B.life -= 1
        
    else:
        print_sleep(f'\nTeam:{B.id} win the war!')
        print_sleep(f'Team:{A.id} lose the war!\n')
        A.life -= 1
           

