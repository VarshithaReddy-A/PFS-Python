#loops
#for,while,range,break,continue,pass
'''
a=[10,20,30,40,50]
for i in a:
    print(i)
'''
'''
a=[10,20,30,40,50,60]
for i in a:
    print(a)
'''
'''
a=[10,20,30,40,50,60]
for i in a:
    print(i)
    print(a)
    print(type(a))
    print(type(i))
'''
'''
a=[10,20,30,40,50,60]
for i in a:
    print(i)
    print(a)
print(type(a))
print(type(i))
'''
'''
a=[10,20,30,40,50,60]
for i in a:
    print(i)
print(type(a))
print(type(i))
'''
'''
a=(10,20,30,40,50,60)
for i in a:
    print(i)
print(type(a))
print(type(i))
'''
'''
a={10,20,30,40,50,60}
for i in a:
    print(i)
print(type(a))
print(type(i))
'''
'''
d={"year":2026,"month":"july","date":10}
for i in d:
    print(i)
    print(d)
for i in d.keys():
    print(i)
    print(type(d))
    print(type(i))
for i in d.values():
    print(i)
    print(type(d))
    print(type(i))
for i in d.items():
    print(i)
    print(type(d))
    print(type(i))
'''
#using strings
'''
a="codegnan"
for i in a:
    print(i)
'''
#using float
'''
a=[3.4,5.6]
for i in a:
    print(i)
print(type(i))
print(type(a))
'''
#using
'''
a=["python","java","html","css"]
for i in a:
    print(i)
print(type(a))
print(type(i))
'''
#using complex
'''
a=[5+9j,2+10j]
for i in a:
    print(i)
print(type(i))
print(type(a))
'''
#using bool
'''
a=[True,False]
for i in a:
    print(i)
print(type(i))
print(type(a))
'''
#Task1
'''
fruits=["apple","banana","mango"]
#print(fruits.upper())-->error (in lists we dont have upper attribute so convert into string.
b=str(fruits)
print(b.upper())
'''
#using for loop
'''
a=["apple","banana","mango"]
b=[]
for i in a:
   b.append(i.upper())
print(b)
'''
#Tak2
'''
a=[10,20,30,40,50,"code"]
a.extend("code")
print(a)
'''
#Task3
'''
a=[2,3,5,6,7]
a.insert(2,4)
print(a)
'''
#Task4-->(5,6,7,8,9) list is immutable so we change to list..
'''
b=(5,6,7,8,9,10)
c=list(b)
c.remove(10)
d=tuple(c)
print(d)
'''
#Task5
'''
e=[7,9,2,0,1,4,9,3,20]
e.sort()
print(e)
'''
#while loop()
'''
a=10
while a>1:
    print(a)
'''
'''
a=10
while a>1:
    print(a)
    a=a-1
'''
'''
a=20
while a>5:
    a=a-1
    print(a)
'''
'''
a=20
while a>5:
    a=a-1
print(a)
'''
'''
a=30
while a>2:
    print(a)
    a+=1
'''
'''
a=30
while a>2:
    print(a)
    a-=1
'''

#voting
'''
while True:
    age=int(input("enter age:"))
    if age>=18:
        print("eligible to vote")
    else:
        print("not eligible to vote")
 '''

'''
range->range function returns a seq of nums,starting from 0, by default and
increments by one by one and stops before a specified num. (0 to n-1)
steps:
1.start
2.stop
3.step
in list we have a limit.. we cant give 100nums at a time.so, we use range
syntax;
for i in range(start,stop,step)
'''
'''
for i in range(10):
    print(i)
'''
'''
for i in range(5,15):
    print(i)
'''
'''
for i in range(30,35):
    print(i,end="")
'''
#task
'''
for i in range(2,19):
  if  i%2==0:
    print(i,end=",")
'''
'''
for i in range(2,20,2):
    print(i,end=",")
'''
'''
for i in range(5,50,5):
    print(i,end=",")
'''
'''
for i in range(0,30,3):
    print(i,end=",")
'''
'''
if marks in range():
    print()
elif
else
'''
'''
marks =int(input())
if marks in range(91,100):
    grade="A"
elif marks in range(81,91):
    grade="B"
elif marks in range(71,81):
    grade="C"
elif marks in range(51,71):
    grade="D"
elif marks in range(51):
    grade="FAil"
print(grade)
'''
'''
while True:
    marks=int(input("enter the marks"))
    for marks in range(91,101):
        print("grade A")
'''        
#break
'''
a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        break
'''
'''
a=30
while a>2:
    a=a-1
    if a==20:
        break
    print(a)
'''
'''
#continue
a=15
while a>3:
    print(a)
    a=a-1
    if a==11:
        continue
'''
'''
a=15
while a>3:
    print(a)
    a=a-1
    if a==11:
        continue
    print(a)
'''
'''
for i in range(18):
    if i==14:
        continue
    print(a)
'''
'''
a="python"
for i in a:
    if i=="t":
        continue
    print(i)
'''
#pass
'''
a=12
while a>4:
    print(a)
    a=a-1
    if a==10:
        pass
'''
'''
for i in range(25):
    if i==10:
        pass
    print(i)
'''
