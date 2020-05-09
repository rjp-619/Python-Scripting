import random

print(random.randrange(50))     #random from 0(by default) to 50

print(random.random())          #random FLOAT VAlue from 0 to 1

print(random.randrange(0,50,5)) #random from 0 to 50 with step size 5



random.seed(5)                  #maps the next random instruction with 5
print(random.randrange(50))


random.seed(5)
print(random.randrange(50))

print(random.choice([1, 4, 8, 10, 3]))  #selects random from given set
