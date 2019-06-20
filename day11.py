Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:\Python\Python37-32\Day 10\hw2.py ================
values inside the function: [1, 2, 3, 4]
local variables are: {'mylist': [1, 2, 3, 4], 'p': 89}
global variables are: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Python\\Python37-32\\Day 10\\hw2.py', 'x': 9, 'y': 7, 'changeme': <function changeme at 0x03890BB8>, 'mylist_var': [10, 20, 30]}
values outside the function: [10, 20, 30]
>>> 
================ RESTART: C:\Python\Python37-32\Day 10\hw2.py ================
values inside the function: [1, 2, 3, 4]
local variables are: {'mylist': [1, 2, 3, 4], 'p': 89}
global variables are: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Python\\Python37-32\\Day 10\\hw2.py', 'x': 9, 'y': 7, 'changeme': <function changeme at 0x03AC0BB8>, 'mylist_var': [10, 20, 30]}
values outside the function: [10, 20, 30]
>>> 
============== RESTART: C:/Python/Python37-32/Day 11/format.py ==============
apple,banana,carrot
apple,banana,carrot
carrot,banana,apple
carrot,banana,banana,apple
c,b,a
apple,banana,apple
coordinates:37.24N,-115.81W
Welcome:Harsh,your college is:VIPS
>>> 
============== RESTART: C:/Python/Python37-32/Day 11/format1.py ==============
Coordinates:37.24N,-115.81W
The complex number (3-5j) is formed from the realpart 3.0 and the imaginary part-5.0.
Traceback (most recent call last):
  File "C:/Python/Python37-32/Day 11/format1.py", line 8, in <module>
    print('X:{0[0]}; Y:{0[1]};abc:{1[0],{1[1]}'.format(coord,abc))
ValueError: unexpected '{' in field name
>>> 
============== RESTART: C:/Python/Python37-32/Day 11/format1.py ==============
Coordinates:37.24N,-115.81W
The complex number (3-5j) is formed from the realpart 3.0 and the imaginary part-5.0.
X:3; Y:5;abc:2,9
first tuple:3,9,secomd tuple:2,4
Apple#########################
#########################Apple
############Apple#############
Traceback (most recent call last):
  File "C:/Python/Python37-32/Day 11/format1.py", line 14, in <module>
    print('{:#*^30}'.format('Apple'))
ValueError: Invalid format specifier
>>> 
============== RESTART: C:/Python/Python37-32/Day 11/format1.py ==============
Coordinates:37.24N,-115.81W
The complex number (3-5j) is formed from the realpart 3.0 and the imaginary part-5.0.
X:3; Y:5;abc:2,9
first tuple:3,9,secomd tuple:2,4
Apple#########################
*************************Apple
            Apple             
************Apple*************
>>> 
============== RESTART: C:/Python/Python37-32/Day 11/format1.py ==============
Coordinates:37.24N,-115.81W
The complex number (3-5j) is formed from the realpart 3.0 and the imaginary part-5.0.
X:3; Y:5;abc:2,9
first tuple:3,9,secomd tuple:2,4
Apple#########################
*************************Apple
            Apple             
************Apple*************
Traceback (most recent call last):
  File "C:/Python/Python37-32/Day 11/format1.py", line 15, in <module>
    print("int:{0:d};hex:{0:x}; oct:{0,o}; bin:{0:b}".format(42,55))
KeyError: '0,o'
>>> 
============== RESTART: C:/Python/Python37-32/Day 11/format1.py ==============
Coordinates:37.24N,-115.81W
The complex number (3-5j) is formed from the realpart 3.0 and the imaginary part-5.0.
X:3; Y:5;abc:2,9
first tuple:3,9,secomd tuple:2,4
Apple#########################
*************************Apple
            Apple             
************Apple*************
int:42;hex:2a; oct:52; bin:101010
int:55;hex:37; oct:67; bin:110111
123,456,780
Correct answers:86.3636%
>>> 
>>> 
=============== RESTART: C:/Python/Python37-32/Day 10/yield.py ===============
>>> x=demo_yield()
>>> type(x)
<class 'generator'>
>>> next(x)
code segment 1 is executed
1
>>> next(x)
code segment 2 is executed
2
>>> next(x)
code segment 3 is executed
3
>>> next(x)
code segment 4 is executed
4
>>> next(x)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    next(x)
StopIteration
>>> 
============== RESTART: C:/Python/Python37-32/Day 11/yield 2.py ==============
i= 0 res= 1
1
i= 1 res= 2
2
i= 2 res= 3
3
i= 3 res= 4
4
i= 4 res= 5
5
i= 5 res= 6
6
i= 6 res= 7
7
i= 7 res= 8
8
i= 8 res= 9
9
i= 9 res= 10
10
i= 10 res= 11
11
>>> 
>>> 
>>> 



>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 


>>> 
>>> 


>>> 
>>> 



>>> 
>>> 


>>> 

>>> 

>>> 

>>> 

>>> 

>>> 

>>> 
>>> 
============== RESTART: C:/Python/Python37-32/Day 11/yield 2.py ==============
i= 0 res= 0
0
i= 1 res= 1
1
i= 2 res= 3
3
i= 3 res= 6
6
i= 4 res= 10
10
i= 5 res= 15
15
i= 6 res= 21
21
i= 7 res= 28
28
i= 8 res= 36
36
i= 9 res= 45
45
i= 10 res= 55
55
>>> 
========= RESTART: C:/Python/Python37-32/Day 11/ternary operator.py =========
1
logout
2
>>> print("code segment 1 is executed")
    yield 1
