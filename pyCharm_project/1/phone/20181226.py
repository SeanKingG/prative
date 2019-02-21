class Tiger():
    def __init__(self,weight = 200):
        self.name = 'tiger'
        self.weight = weight

    def feed(self,food):
        if food in ('meat' , 'M'):
            print('your food is right.')
            self.weight += 10
        else:
            self.weight -=10
            print('your food is wrong.')

    def knock(self):
        print("WOW")
        self.weight -= 5

class Sheep():
    def __init__(self,weight = 100):
        self.name = 'sheep'
        self.weight = weight

    def feed(self,food):
        if food in ('grass','G'):
            self.weight += 10
            print('your food is right.')
        else:
            self.weight -=10
            print('your food is wrong.')

    def knock(self):
        print("mie~~~~~")
        self.weight -= 5

class Room():
    def __init__(self,roomNum,animal):
        self.roomNum = roomNum
        self.animal = animal

def zooFeed(roomNum,rooms,time_start):#定义函数：游客喂食动物
    while True:
        food = input('你想喂什么给这个房间的动物?(肉(M&meat) or 草(G&grass)):')
        if food in ('M','meat','G','grass'):#限制输入的食物
            rooms[roomNum - 1].animal.feed(food)
            Feed = input("想不起继续喂食(Y/N)：")
            if Feed == 'N':
                break
            if time.time() - time0 > 10:
                break
        else:
            if time.time() - time0 > 10:
                break
            print('请喂食正常的食物(肉(M&meat) or 草(G&grass))！')


import random
import time
rooms = []
for roomNum in range(1,11):#随机生成10个房间及动物
    j = random.randint(1,2)
    if j == 1:
        roomObject = Room(roomNum,Tiger())
    else:
        roomObject = Room(roomNum,Sheep())
    rooms.append(roomObject)

time0 = time.time()
while time.time()-time0 <= 180:
    roomNum = random.randint(1, 10)
    while True:#限制用户的输入行为
        action = input("房间号：{},你想做什么?(喂食(F&feed) or敲门(K&knock)):"
                                .format(roomNum))
        if action not in ('F','feed','K','knock'):
            print('请输入F、feed、K、knock中的字符或字符串.')
        else:
            break
    if rooms[roomNum - 1].animal.weight <= 0:  # 体重为0或者小于0的视为死亡，无法参与活动
        print('这个房间的动物已经死了')
        break
    if action in ('knock', 'K'):#敲门动作
        rooms[roomNum - 1].animal.knock()
        feedConfire = input('你想给喂这间房的动物东西吃么(Y/N):')
        if feedConfire == 'Y':#敲门后喂食
            zooFeed(roomNum, rooms,time0)
    if action in ('feed','F'):#不敲门确认，直接喂食
        zooFeed(roomNum, rooms,time0)



print('the game is over!')
for room in rooms:#遍历输出各房间动物种类及体重
    print('房间号:{} \t动物:{}\t体重:{}'.format(room.roomNum,room.animal.name,room.animal.weight))


