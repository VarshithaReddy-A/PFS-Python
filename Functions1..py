#Functions
'''
a=16
b=30
print("sum of num:", a+b)
print("dif of num:", a-b)
print("Mul of num:", a*b)
a=45
b=90
print("sum of num:", a+b)
print("dif of num:", a-b)
print("Mul of num:", a*b)
a=56
b=34
print("sum of num:", a+b)
print("dif of num:", a-b)
print("Mul of num:", a*b)
'''
'''
def caluculator(a,b):
    print("sum of num:", a+b)
    print("dif of num:", a-b)
    print("Mul of num:", a*b)
caluculator(10,20)
caluculator(100,200)
'''
#task sum
'''
def calc(a,b):
    print("pow of nums:", a**b)
    print("mod of num:", a%b)
    print(" int div of num:", a//b)
calc(3,5)
calc(7,8)
'''

'''
def calc(a,b):
    print("sum of nums:", a+b)
calc(3,5)
'''
#using runtime-->contineous execution using loop(while)
'''
while True:
    def add():
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(a+b)
    add()
 '''
#Recursive function-->A function calls itself
'''
def add():
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)
    add()
add()
'''
#using string- concatination
def fullname():
    fname=input("enter fname:")
    lname=input("enter lname:")
    print((fname+""+lname).title())
fullname()
