#Voting
'''
age=int(input("enter age:"))
if age>=18:
    print("Eligible to Vote")
else:
    print("Not eligible to vote")

'''

#even or odd

'''
a=int(input("enter num:"))
if a%2==0:
      print("even number")
else:
    print("odd number")
'''

#leap year
'''
year = int(input("Enter year: "))
if year%4==0:
    print("Leap year")
else:
    print("Not leap year")
'''

#guest code
'''
name=input("enter name:")
if name=="varshi":
    print("welcome pooja")
else:
    print("welcome guest")
'''
'''
name=input("enter name:").lower()
if name=="varshi":
    print("welcome",name)
else:
    print("welcome guest")
'''

#using 5users

'''
name=input("enter name:").lower()
if name=="varshi":
    print("welcome",name)
elif name=="sita":
    print("welcome",name)
elif name=="latha":
    print("welcome",name)
elif name=="pooja":
    print("welcome",name)
elif name=="geetha":
    print("welcome",name)
else:
    print("welcome guest")
'''
#simple way
'''
names=["sita","latha","pooja","geetha","thanu"]
a=input("enter name:").lower()
if a in names:
    print("welcome",a)
else:
    print("welcome guest")
'''

#vowels
'''
vowels=['a','e','i''o','u']
i=input("enter letter")
if i in vowels:
    print("it is vowel")
else:
    print("it is not vowel")
'''

'''
letters=['a','e','i','o','u']
word=input("enter a letter")
if word==letters:
    print("vowel")
else:
    print("consonant")
'''

#social media login-->using if-else
'''
username=input("enter username:")
password=int(input("enter password:"))
if username=="varshi" and password==1234:
    print("login sucessful")
else:
    print("invalid credentials")
'''
'''
username=input("Enter username: ")
password=int(input("Enter password: "))
if username=="varshi":
    if password==1234:
        print("Login successful")
else:
    print("Invalid username")
'''
#social media login -->(using nested-if)
'''
username=input("Enter username: ")
password=int(input("Enter password: "))
if username=="varshi":
    if password==1234:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")
'''

'''
username=input("enter username:")
password=input("enter password:"))
if username=="varshi" and password==varshi@29:
    print("login sucessful")
else:
    print("invalid credentials")
'''
#multiple-if
'''
age=int(input("enter age:"))
marks=int(input("enter marks:"))
attendance=int(input("enter attendance:"))
if(age>=18):
    print("eligible for vote")
if(marks>=80):
    print("eligible for scholarship")
if(attendance>=70):
    print("allowed to write exam")
'''
#if-else
'''
age=int(input("enter age:"))
marks=int(input("enter marks:"))
attendance=int(input("enter attendance:"))
if(age>=18):
    print("eligible for vote")
else:
    print("not eligible to vote")
if(marks>=80):
    print("eligible for scholarship")
else:
    print("not eligible for scholarship")
if(attendance>=70):
    print("allowed to write exam")
else:
    print("not allowed to write exam")
'''
