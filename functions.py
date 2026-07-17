'''
def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    print("per head bill is {}".format(b//a))
    print(f"perhead bill is {b//a}")
splitbill()
'''
'''
def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    c=b//a
    print("per head bill is {}".format(c))
    print(f"perhead bill is {c}")
splitbill()
'''
'''
while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        options=int(input( choose the option
                            1.Add
                            2.Sub
                            3.Mul))
        if options==1:
            print("Addition:",a+b)
        elif options==2:
            print("Substraction:",a-b)
        elif options==3:
            print("multiplication:",a*b)
        else:
            print("In valid option")
    cal()
'''
'''
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input(choose the option
                            1.add
                            2.sub
                            3.mul))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()
'''
'''
#keyword and positional arguments
def Details(id,name,mailid):
    id=10
    name="varshi"
    mailid="varshi@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
'''
'''
def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id="20",name="VARSHI",mailid="varshi@gmail.com")
Details(20,"varshi","varshi@gmail.com")
Details(40,"vamsi","vamsi@gmail.com")
Details("h@gmail.com",50,"harika")
Details(id="10",name="harshi",mailid="harshi@gmail.com")
'''

#default aurgument-->cannot be  changed
'''
def Grocery(item,price):
    print("item is %s" item)
    print("price is %.2f" %price)
Grocery("rice",1500)
'''

'''
def Grocery(item="sugar",price=100):
    print("item is %s" item)
    print("price is %.2f" %price)
Grocery()
'''

'''
def Grocery(item,price=100):
    print("item is %s" item)
    print("price is %.2f" %price)
Grocery("dhal")
'''

'''
def Grocery(item="ghee",price): #shows error
    #non def arg follows def arg
    print("item is %s" item)
    print("price is %.2f" %price)
Grocery(500)
'''

'''
#cake_name,price,qty
def cake(item,price,qty):
    print("item is %s" %item)
    print("price is %d" %price)
    print("qty is %s" %qty)
cake(item="redvelvet",price=800,qty="1kg")
'''

'''
def cake(item="chocolate",price=400,qty): #error ->non default aurg  follows default aurg
    print("item is %s" %item)
    print("price is %d" %price)
    print("qty is %s" %qty) 
cake(item,price,qty="1kg")
'''
'''
def cake(item,price=500,qty="1kg"):
    print("item is %s" %item)
    print("price is %d" %price)
    print("qty is %s" %qty)
cake("redvelvet")
'''

#* arguments(* is used to unpack the elements)
'''a=[10,20,30,40,50]
print(a)
print(*a)'''#output displayed without list

'''
b=(10,20,30,40,50)
print(b)
print(*b)
'''

'''
c={10,20,30,40,50}
print(c)
print(*c)
'''
'''
d={"name":"varshi","year":2026,"month":7}
print(d)
print(*d) '''#returns only keys

'''
a="codegnan"
print(a)
print(*a)''' #divides into char's

'''
a,b,c=2,3,4,5,6,7,8,9,10
print(a) #error
print(b)
print(c)
'''
'''
a,b,c=3,4,5
print(a)
print(b)
print(c)
'''
'''
a,b,*c=2,3,4,5,6,7,8,9,10
print(a) 
print(b)
print(*c)
'''
'''
*a,b,c=2,3,4,5,6,7,8,9,10
print(*a) 
print(b)
print(c)
'''
'''
a,b,c="codegnan"
print(a) 
print(b)
print(c) ''' #error

'''
a,b,c="cod"
print(a) 
print(b)
print(c)
'''

'''
*a,b,c="codegnan"
print(*a) 
print(b)
print(c)
'''
'''
a,*b,c="codegnan"
print(a) 
print(*b)
print(c)
'''
