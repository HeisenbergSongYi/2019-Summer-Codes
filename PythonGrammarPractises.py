"""
a = int(input("A:"))
b = int(input("B:"))
c = int(input("C:"))
d = int(input("D:"))
e = int(input("E:"))

max =a

if(max<b):
   max=b
if (max<c):
   max=c
if (max<d):
   max=d
if (max<e):
   max=e

print("max value is:", max)
"""

"""
x = int(input("X:"))

y=0

if (x<0):
    y = -1
if (x == 0):
    y= 0
if (x>0):
    y= 1

print (y)
"""

"""
sum = 0
for i in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+i
    print (sum)
"""
"""
list = range(1,-10,-1)

sum =0
for i in list:
    sum =sum+i
    print (sum)
"""
"""
for i in "China":
    print(i)
"""

"""
d = { "key1" : "value1", "key2" : "value2"}

d["key3"] ="GZ"

print(d)

a = {"key4" : "value3"}
a.update(d)


for i, j in d.items():
    print(i+"up")
    print(j+"down")

a.pop("key1")
print(id(a))
print(id(d))

print (d)
print (a)
"""
"""
a = [1,2,3,4,5,1,1,1,1,1,1]
a.append(6)

b= [2,3,4,5,6]

b.pop(0)
reverse (a)
a.extend(b)
print (a)
b =a.count(1)
print (b)
"""

"""
asterisk = range(1,50,1)

n= 50
for i in asterisk:
    print (i*"*")
    print(' ' * (n - (i - 1)) + '*' * (2 * i - 1))
"""

"""
s = "The World"
r=s.split(" ")
print (r)
"""

"""
str = "-"
seq = ("a", "b", "c")
print (str.join( seq ))

"""

"""
r = " My"
r.lstrip()
seq = r.lstrip()
print (seq)
"""

"""
x,y = "py", "C++"
x,y = y,x
"""

"""
f = open("E://shit.txt",'wr')
type(f)
f.write("shitshitshi")
f.__next__()
f.close()
"""

"""
a=[1, 0, 0, 2, 3, 0]
b=["Apple", "banana", "Orange", "pineapple", "pear", "peach"]
c= []
d= []

for i in range(len(a)):
    if a[i]!=0:
     c.append(a[i])
     d.append(b[i])

print (c,d)
"""


"""
def fuckingjackass (a,b):
  c = []
  d = []
  for i in range (len(a)):
   try:
     c=a.index(0)
     a.pop(c)
     b.pop(c)
   except:
     break

  print (a,b)


a = [1, 9, 0, 2, 3, 9]
b = ["nmsl", "jiba", "touzi", "penis", "dick", "tits"]

fuckingjackass(a,b)
"""

"""
def my(a):
    b=a+3
    print (b)

my(6)
"""

"""
def add(x,y):
     z = x+y
     print(z)

a=1
b=2
add(a,b)
"""

"""
def mydick(a,*b):
    a.pop(0)
    for i in b:
        print (a,b)

mydick([8,9,90],[1,3,4,5,6,7,8,9,0,9,9,9,9,9],[345432,577],[123,546745],[123,"m45"])
"""
'''
b = input("input your fucking penis")

print(b)
'''
# coding=uft-8

"""
name = input("What is your fucking name?")
age = input("what is your stupid age?")

print("Dear", name, "You are a piece of shit")
print("You have been shitting for", age,"years")

after_ten = int(age)+10
print ("You will be fucking" + str(after_ten)+ "years after a decade")

"""

"""
import math
p = math.pow(3,2)
print(p)
"""
"""
import os
d = os.mkdir("shift")
"""

"""
f = open("shit.txt")
for line in f:
    print (line, end='')
for line2 in f:
    pint (line2)
"""

"""
def add_function(a,b):
    c = a+b
    print(c)
    return c

add_function(33,9)
"""

"""
def fibs(n):
    result = [0,1]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    return result

result = fibs(10)
print(result)
"""
"""
def my_fun():
  
    This is my function 
 
    print ("I am your dad")

c = my_fun.__doc__
print(c)
"""

"""
def foo(x, *args):
    print ("x:",x)
    print ("tuple:",args)


foo(7,9,"code")
"""
"""
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

f = fib(3)
print (f)
"""
"""
def bar():
    print("I am function bar")

def foo(func):
    func()

foo(bar)
"""

"""
def convert(func, seq):
    return[func(i) for i in seq]

def num(n):
    if n%2 == 0:
        return n**n
    else:
        return n*n

myseq = (111, 222, 333)
r = convert(num, myseq)
print(r)
"""
"""
def foo():
    def bar():
        print ("bar is running")
    bar()
    print ("foo is running")

foo()
"""
"""
def foo():
    a =1
    def bar():
        nonlocal a
        a = a+1
        print ("bar()a=",a)
    bar()
    print ("foo()a",a)

foo()
"""

"""
def maker(n):
    def action(x):
        return x**n
    return action


f = maker(2)
print(f)
m = f(3)
print(m)
"""

""""
def foo(**kargs):
    print (kargs)

foo(a=1,b=2,c=3)
"""

"""
def book(author, name):
  print ("{0}is writing {1}".format (author,name))

bars = {"name":"hOW To Eat Shit", "author":"Hsb"}
book(**bars)
"""
"""
def foo (x,y=2,*targs,**dargs):
    print("x==>",x)
    print("y==>",y)
    print("tuple==>",targs)
    print("dict==>",dargs)

foo(2,3,"ring","of","elysium",do="1",re="2",mi="3")
"""
"""
for i in [1,2,3,4]:
    print(i, end=',')
import math
pow(3,2)
sqrt(9)
"""
"""
print("guess what # i want")
number =int(input())

if number==10:
    print("thats corret, I mean {}".format(number))
    print('fucking smart ass huh?!')
elif number<10:
    print("number too small")
elif number>10:
    print("number too fucking big")
else:
    print("suck my dick plz")
"""
"""
x = 9
y= 42
name = "fuck" if pow(x,2) <y else "damnit"
print(name)
"""
"""
hello = "ringofelysium"
for i in hello:
    print(i,end='')
"""
"""
hello = "world"
for i in range(len(hello)):
    print (hello[i])

ls_lander = ["Hello", "I am your dad", "Son if a bitch", ""]
for shit in ls_lander:
    print(shit)


for i in range(len(ls_lander)):
    print(ls_lander[i])
"""

"""
ass = list(range(0, -9, -1))
print(ass)
"""

"""
a = len(["I", "am", "a", "pythoner", "I", "am", "learning", "it", "with", "qiwsir"])
anus = list(range(a))
print(anus)
"""
"""
for i in range(1,100):
    a =i%3
    if a==0:
        print(i)
"""

"""
a=[1,2,3,4,5]
b=[9,8,7,6,5]
for dick in range(len(a)):
    thigh = a[dick]+b[dick]
    print(thigh)
"""
"""
c = [1,2,3]
d = [4,5,6,7,8]
fucking_hell = list(zip(c,d))
print(fucking_hell)
"""

"""
a=[1,2,3,4,5]
b=[9,8,7,6,5]
for a,b in list(zip(a,b)):
    n = a+b
    print(n)
"""

"""
a=[1,2,3,4,5]
b=[9,8,7,6,5]
nmsl=[]

for x,y in list(zip(a,b)):
    nmsl.append(x+y)

print(nmsl)
"""
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b=["python","www.itdiffer.com","qiwsir","cnmlgbnmsl?"]
nmsl=[]
length = len(a) if len(a)<len(b) else len(b)
for n in range(length):
    nmsl.append(str(a[n])+b[n])
print(nmsl)
"""
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b=["python","www.itdiffer.com","qiwsir","cnmlgbnmsl?"]
cnmb=[]

for x,y in list(zip(a,b)):
    cnmb.append(str(x)+y)

print(cnmb)
"""
"""
myinfor = {"name":"qiwsir",	"site":"qiwsir.github.io", "lang":"python"}
infor = {}
for k,v in myinfor.items():
    infor[v]=k

print(infor)
"""

"""
myinfor = {"name":"qiwsir",	"site":"qiwsir.github.io", "lang":"python"}
fuckoff = list(zip(myinfor.values(), myinfor.keys()))


print(fuckoff)
print(myinfor)
"""
"""
week = ['monday', 'sunday', 'friday']
for i in range(len(week)):
    print((week[i])+' is '+str(i))

"""

"""
week = ['monday', 'sunday', 'friday']
for (i,shit) in enumerate(week):
    print(shit+ 'is' +str(i))
"""

"""
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
"""

"""
raw = 'Can you go fuck yourself? Or let a prostitute fuck you?'
raw_list = raw.split(" ")
temp = raw_list

for i,string in enumerate(raw_list):
    if "fuck" in string:
        raw_list[i]= "****"
sentence = " ".join(raw_list)
print(sentence)
"""

"""
power2 = []
for i in range(1,10):
    power2.append(i*i)

print(power2)

"""
"""
squares = [x**2 for x in range(1,100)]
print(squares)
"""
"""
remainders = [x**2 % 5 for x in range(1,101)]
print(remainders)
"""
"""
myass = ['     glass','apple ','greenleaf    ']
mynewass = [word.strip() for word in myass]
print(mynewass)
"""
"""
i = 666
[i for i in range(9)]
print(i)
"""

"""
guess=0
while guess<3:
    print("input your age")
    age = input()
    if not age.isdigit():
        print("I need a fucking integer")
    elif int(age)<0 or int(age)>=100:
        print("I need a fucking number between 1 and 100! Fuck you, jackass!")
        pass
    else:
        age = int(age)
        if age > 60 and age <100:
            print("u are free to retire")
        else:
            print("u cannot retire")
    print("end of one round")
    guess += 1
"""

import random
i = 0
xnumber = random.randint(0, 9)

while i <10:
    number = input("guess a number between 1-9")
    if not number.isdigit():
        print("I need a fucking integer")
        break
    if int(number)<0 and int(number)>9:
        print("That number is between zero and nine")
        break
    x = 10 -i
    number = int(number)
    if number == xnumber:
        print("nice bitch you are correct! Damn it!")
    if number <  xnumber:
        print("No, fucking no! That number is bigger!")
    if number >  xnumber:
        print("No, that fucking number is smaller! Blyat")

    i += i
    continue

