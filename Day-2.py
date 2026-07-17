Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
#Assignment op
a=3
b=5
a+=b
a
8
a-=2
a
6
a//=2
a
3
a**=4
a
81
a*=4
a
324
b+=2
b
7
b-=4
b
3
b//=2
b
1
b**=3
b
1
b*=4
b
4
b%=6
b
4
b/=2
b
2.0
#comparision Op
a=4
b=8
a<b
True
a>b
False
b<a
False
b>a
True
a==b
False
a=8
b=8
a==b
True
a>=b
True
b<=b
True
a!=b
False
a=3
b=6
a!=b
True
a==b
False
#logical
a=5
b=7
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a>=b or a<=b
True
a!=b or a==b
True
not True
False
not False
True
#identify
a=4
type(a)
<class 'int'>
type(a) is int
True
type(a) is not int
False
a=5.6
type(a) is float
True
type(a) is not float
False
name="varshi"
type(name) is string
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    type(name) is string
NameError: name 'string' is not defined
type(name) is str
True
type(name) is not str
False
a=2+3j
type(a) is complex
True
type(a) is not complex
False
a=3j
type(a) is complex
True
a=True
type(a) is bool
True
a=False
type(a) is bool
True
type(a) is not bool
False
a=10>5
type(a)
<class 'bool'>
type(a) is not bool
False
#membership op
>>> a=4,2,5,7,9,1,0
>>> 8 in a
False
>>> 5 in a
True
>>> 8 not in a
True
>>> a=5
>>> b=7
>>> a&b
5
>>> bin(2)
'0b10'
>>> bin(4)
'0b100'
>>> bin(7)
'0b111'
>>> a=2
>>> b=4
>>> a&b
0
>>> a|b
6
>>> a^b
6
>>> a~b
SyntaxError: invalid syntax
>>> ~a
-3
>>> ~b
-5
>>> a=4
>>> -(a+1)
-5
>>> a=-6
>>> a
-6
>>> ~a
5
>>> a=3
>>> a<<2
12
>>> a>>2
0
>>> a<<3
24
