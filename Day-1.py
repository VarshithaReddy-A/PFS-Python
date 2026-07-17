Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> first name="varshi"
SyntaxError: invalid syntax
>>> first_name="varshi"
>>> print(first_name)
varshi
>>> firstname="varshi"
>>> print(firstname)
varshi
>>> fname="varshi"
>>> lname="ch"
>>> print(fname+lname)
varshich
>>> print(fname+" "+lname)
varshi ch
>>> name="varshi"
>>> print(name)
varshi
>>> city="vja"
>>> print(city)
vja
>>> a=5
>>> print(a)
5
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> name="varshi"
>>> print(name)
varshi
>>> NAME="varshi"
>>> print(NAME)
varshi
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
print(name)
varshi
