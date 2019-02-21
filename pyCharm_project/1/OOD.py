class Tiger:
    name = 'tiger'
    def __init__(self,weight = 200):
        self.weight = weight
    def roar(self):
        print("WoW!!!")
        self.weight -= 5
    @staticmethod
    def roar2():
        print('wow!!')
class Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal
# tiger1 = Tiger(300)
# print(tiger1.name)
# tiger1.roar()
# tiger1.roar()
# tiger1.roar()
# tiger1.roar2()
# tiger1.name = 'fegege'
# print(tiger1.name,tiger1.weight)

# t1 = Tiger(300)
# room1 = Room(1,t1)
# print(room1.num,room1.animal.name)

from random import randint
print(randint(0,1))
print(randint(1,10))
import  time
cuitime = time.localtime()
print(cuitime)
room = []
asd: int
for p in range(0, 10):
    a = randint(0,1)
    if a == 1:
        room.append(Room(p + 1, '娄浩'))
    elif a == 0:
        room.append(Room(p + 1, '王斌'))
for j in range(1,11):
    print(room[j-1].num,room[j-1].animal,'拉稀')
dog = int(input('please input number:'))
print('第{}间房住的是{},他喜欢拉稀'.format(room[dog-1].num,room[dog-1].animal))