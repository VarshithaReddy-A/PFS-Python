#variable length arguments
'''
def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[2,3,4,5,6,7]
check(*b)
c={7,8,9,10,11}
check(*c)
d={"year":2026,"month":7}
check(*d)
'''

'''
def check1(*a):
    d=1 #creating a variable
    print(a) #stores 2,3,4,5,6,7 values
    for i in a:
        d=d+i
        print(d)
check1(2,3,4,5,6,7)
check1(2,3,4,5,3.2,5.6)
check1(2,3,4,5,6,7,"varshi") #error
'''
'''
def check1(*a):
    d=1 #creating a variable
    print(a) #stores 2,3,4,5,6,7 values
    for i in a:
        if type(i) in (int,float):
        d=d+i
        print(d)
check1(2,3,4,5,6,7)
check1(2,3,4,5,3.2,5.6)
check1(2,3,4,5,6,7,"varshi"5+9j,False) #error
'''

#Keyword variable length arguments(**)--->dict
'''
def details(**a):
    print(a)
    print(type(a))
    for i in a:
       print(i)
    for i in a.keys():
          print(i)
    for i in a:
          print(a[i])
    for i in a.values():
          print(i)
    for i in a:
          print(i,a[i])
    for i in a.items():
          print(i)
d={"name":["varshi","sita","latha"],"branch":["cse","ds","it"],"rollno":[20,30,40]}
details(**d)
'''
'''
def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(i)
    for i,j in b.items():
        print("key is:", i)
        print("value is", j)
final()
data=(2,3,4,5,2.3,4.5)
final(*data)
d={"name":["varshi","sita","latha"],"branch":["cse","ds","it"],"rollno":[20,30,40]}
final(**d)
final(*data,**d)
'''

def railway():
    
