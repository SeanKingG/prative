class Dog():
    def __init__(self, name, age, weight=100):
        Dog.name = name
        Dog.age = age
        Dog.weight = weight
    def beat(self,animal):
        print('your dog {} beat {},he is {} years old.'.format(Dog.name.title(),animal,Dog.age))

Bob = Dog('bob',17,90)
Bob.beat('mouse')