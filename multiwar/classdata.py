import random
import time

# @dataclass
class Team:  
    number = 0
    def __init__(self, id, life, money, military, farmer, army):   #self是变量，我也可以换成其他名字，但一般都用self
        self.id = id
        self.life = life   #如果指定TeamA，就是Team.life = 2（这是self的意思）
        self.money = money
        self.military = military
        self.farmer = farmer
        self.army = army
        Team.number += 1


    def __str__(self):   #当有人call整个Team，会return这个值
        return f'id:{self.id}, life:{self.life}, money:{self.money}, military:{self.military}, farmer:{self.farmer}, army:{self.army}'
    
    
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
        

class ActionMenu:  
    def __init__(self,act):   #这里的self是ActionMenu的变量，act是Team的变量
        self.act=act

    def actionfunction(self,index):   #当输入ActionMenu.Make_Money.actionfunction，就会返回self.make.money，执行制定的def
        if index <=2:
            return self.act.proceed(index)
        else :
            actionname = '','Start a war'
            return actionname 
         
# def start_a_war(A, B):
#     winner = random.choices([A,B],weights=[A.military,B.military],k=1)   #weight是胜负的概率   #要用choices而不是choice，因为有概率计算
#     time.sleep(1)
#     if winner == [A]:   #一定要[A]而不是A，因为choice的是一个list
#         print('You win the war!\n')
#         B.life -= 1
#     else:
#         print('You lose the war!\n')
#         A.life -= 1

