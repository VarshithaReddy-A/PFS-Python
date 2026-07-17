#list comprehension
a=["codegnan","python","course"]

#print(a.upper())-->error

'''b=str(a)
print(b.upper())'''

'''for i in a:  #data is not in list 
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#a=[expr for var in collection/range]
'''
a=[i.upper() for i in a] 
print(a)

'''
'''
a=["vja","hyd","vzg"]
#["Vja","Hyd","Vzg"]
b=str(a)
print(b.title())
'''
'''
a=["vja","hyd","vzg"]
b=[i.title() for i in a]
print(b)
'''
'''a=[1,2,3,5,6,8,12,13]
#[1,4,9,25,36,64,144,169]
b=[i*i for i in a]
b=[i**2 for i in a]
b=[pow(i,2) for i in a]
print(b)'''

#if-usage in list comprehension
'''a=[]
for i in range(16):
    #print(i*i,end=" ")--->without list
    a.append(i*i) #--->with list
print(a)'''
'''
a=[i for i in range(16) if i%2==0]
print(a)

b=[i for i in range(16) if i%2!=0]
print(b)
'''
'''
#print 0-30
a=[i for i in range(31)]
print(a)'''

'''
fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"] #with 'a' words in alist
a=[i for i in fruits if 'a' in i]
print(a)
'''
'''
fruits=["apple","banana","grapes","kiwi","mango","dragon","berry"]  #without 'a' words in a list
a=[i for i in fruits if 'a' not in i]
print(a)
'''
'''
result = [i*i if i % 2 == 0 else i*5 for i in range(21)]
print(result)
'''
'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
#print(a+b)
c=[a[i]+b[i] for i in range(5)]
print(c)
'''
