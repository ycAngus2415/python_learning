#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'this my learning of python3'

__author__='yangchao'


100+100
print('hello,world!')
print('The quick brown fox','jumps over','the lazy dog')
print(300)
print(200+300)
print('100+200=',100+200)
name='michael'
print(name)

print('hello',name)#print可以用逗号表示多个输出的空格。相当于
print('hello '+name)

print(1024*768)

a=100

if a>=0:
    print(a)
else:
    print(-a)


print(10/3)
print(10//3)


print('I\'m ok')
print('I\'m learning\nPython.')

print('\\\n\\')

print(r'\\\t')
print('''
line2
line3''')
a=True
print(a)

print(True or False)

print('true and false :',True and False)

if True :
    print(r"It's true")

print(None)

a=1
print(a)

t='oo7'
print(t)
print(a+2)

a='abc'

b=a
a='cde'

print(a)
#在给变量赋值常量的时候，是先创建这个常量的对内存，然后对引用
print(b)

print(10//3)

print(10%3)

n=123
f=456.789
s1='Hello,world'
s2='Hello,\'Adam\''
s3=r'Hello,"bart"'
s4=r'''Hello,''
'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

print(len('this si'))
x='hello, %s ,your fee is %d in %d month, the rest is %d'
print(x%('yangchao',5,12,4))#可以用两个%%来表示转义

x='xiaoming'
print(x)#这里应该是这个插件的问题，它可能指定了编译一定使用ascii。中文在这里不支持

#list

classmates=['yangchao','sunsijia','zhangyi']

print(len(classmates))
for i in classmates:
    print(i,'is a classmates')

print(classmates[-1])
classmates.append('qinzheng')
print(classmates[-1])

classmates.insert(1,'lumenglong')

for i in classmates:
    print(i)


print(classmates.pop())

print('\n')
for i in classmates:
    print(i)

print(classmates.pop(1))
classmates[2]='zy'
print(classmates[2])


x=('yangchao','sunsijia')
print(x)

print((1,))


L=[
['Apple','Google','Microsoft'],
['Java','Python','Ruby','PHP'],
['Adam','Bart','Lisa']
]
print(L[0][0])

print(L[1][1])

print(L[2][2])



#condiction

age=20
if age>=18:
    print('your age is ',age)
    print('adult')
elif age >=6:
    print('kid')
else:
    print('your age is ',age)
    print('teenager')


str1='1000'

birth=int(str1)
print(birth)


high=1.75
weight=80.5
ibm=weight/high**2
if ibm<18.5:
    print('too low')
elif ibm<25:
    print('nomal')
elif ibm<28:
    print('too heavy')
elif ibm<32:
    print('pawn')
else :
    print('overpawn')
sum=0
for i in range(10):
    sum+=i

print(sum)

L=['Bart','Lisa','Adam']
for i in L:
    print('hello',i)

d={'mac':32,'bob':34,'yang':20}
print(d['mac'])
#dict 存在一个索引表。
print(d.pop('bob'))
print(d)

s=set([2,3,4])
print(s)
s.add(2)
print(s)
s.add(5)
print(s)
s1=set([4,5,7])
print(s1&s)
print(s1 |s)
#set 和dict 索引的都是不可变对象。
s=set([2,3])
print(s)
x=[3.0,4,5]

class Circle(object):
    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14*self.r**2

    def round(self):
        return 2*3.14*self.r

s=Circle(3)
print(s.area())
print(s.round())


def nop(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x is not a int of float or int')
    if x>0:
        return x
    else :
        return -x

nop(3)
x=[1,2,3]
import math
print(math.sin(3))

def quadratic(a,b,c):
    return(-b-math.sqrt(b**2-4*a*c))/(2*a),(-b+math.sqrt(b**2-4*a*c))/(2*a)

print(quadratic(2,3,1))

#可变参数直接一个参数就定义了所有的变量
def sums(*numbers):
    s=0
    for i in numbers:
        s+=i
    return s

print(sums(2,3,4))
#函数的参数
def power(x):
    return x*x
print(power(5))
print(power(34))

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(2,3))

print(power(3,5))
#默认参数
def power(x,n=2):
    s=1
    while n>0:
        s*=x
        n-=1
    return s
print(power(3))

print(power(3,5))

def enroll(name,gender,age=6,city='beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('yangchao','male')

import sys
import io
print(sys.getdefaultencoding())
print(sys.stdin.encoding)
print(sys.stdout.encoding)
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
print('男')
enroll('yangchao','male',city='changsha')
enroll('yangchao','male',)

def add_end(L=[]):
    if L==None:
        L=[]
    L.append('end')
    return L

print(add_end())
print(add_end())
#加入可变参数的函数
def addd(*numbers):
    s=0
    for i in numbers:
        s+=i
    return s


print(addd(1,2,3,4))
list1=[1,2,3]#可以将list编程可变参数传递给函数
print(addd(*list1))

#关键字参数,命名关键字参数,如果没有*,city和wife就变成位置参数了，命名关键字参数在传递的时候必须要指定参数名
def people(name,age,*,city='chengdu',wife):
    print('name:',name)
    print('age',age)
    print('city',city)
    print('wife',wife)

people('yangchao',16,city='chengdu',wife='sunsijia')
#还可以自己定义一个dict
#my={'city':'mianyang','wife':'ssj','job':'computer'}
my={'city':'mianyang','wife':'ssj'}
people('yangchao',24,**my)
people('yangchao',24,city='mianyang',wife='ssj1')
def person(name,age=14,*arge,city,**other):
    print('name:',name)
    print('age:',age)
    s=0
    for i in arge:
        s+=i
    print('arge',s)
    print('city',city)
    print('others',other)

arge=[5,4,6]
#其实命名关键字参数和关键字参数是一样的，只是需要一定指定参数名，且命名关键字参数必须有
otehr={'job':'computer','like':'swimming'}
person('yangchao',24,*arge,city='mianyang',**otehr)

#递归可能会溢出，但是尾递归不会出现溢出，消耗内存小。尾递归不能返回表达式，只能返回函数本身

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

def fact_iter(n,product=1):
    if n==0:
        return product
    else:
        return fact_iter(n-1,n*product)

print(fact_iter(5))

#切片
L=['yangchao','mianyang',15,'computer']
l=list(range(10))
print(l[1::2])

#迭代
from collections import Iterable
print(isinstance(l,Iterable))

l=[(1,2),(3,5),(7,1),(3,6)]
for x,y in l[1::2]:
    print(x,y)

#列表生成式只能生成列表
l=[x**2 for x in range(10) if x**2%2==0]
stri=['xyz','yangchao','sunsijia','love']

print(l)

ss=[m+n+y for m in stri for n in stri for y in stri]
print(ss)
if 'yangchaolovesunsijia' in ss and 'sunsijialoveyangchao' in ss:
    print(True)
s='yangchao'
print(s.upper())
ll=['hello','world',18,'apple',None]
LL=[s.upper() for s in ll if isinstance(s,str)]
print(LL)

#如果用（）那就是生成器了。是可迭代的，也可以用next
LL=(s.lower() for s in LL)
print(LL)
for i in LL :
    print(i)
#当有yield这个函数就是一个generator
def feb(n):
    a,b=0,1
    while(n>0):
        yield b
        a,b=b,a+b
        n-=1
#yeild 就是表示一个生成器的输出
for i in feb(5):
    print(i)

#高阶函数
def ss(feb,n):
    print('this is ss')
    for i in feb(n):
        print(i)

ss(feb,5)

l=[1,2,3,4]
def fn(x,y):
    return x*10+y

from functools import reduce
r=reduce(fn,l)#reduce 函数非常强大，能直接将传递函数，将函数结果作为参数继续传递。
print(r)

def x_p(x):
    return x**2

m=map(x_p,l)
print(list(m))

strr=['this ', 'is ', 'my', 'favorite']
def my_upper(x):
    return x.upper()

s=map(my_upper,strr)
print(list(s))

def up_lower(x):
    return x[0].upper()+x[1:].lower()

l=['adam','LISA','barT']
ss=map(up_lower,l)
print(list(ss))


def prod(ll):
    return reduce(lambda x,y:x*y,ll)

s=[3,5,7,9]
print(prod(s))


#内置函数filter就是过滤的意思，当真的时候保留，否则舍弃

#埃氏筛法
def odd_iter(t):
    n=1
    while n<t:
        n+=2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def prime(t):
    it=odd_iter(t)
    i=2
    yield i
    while i<t:#这里不能用for循环，在for里面，it是不会更新的
        i=next(it)
        yield i
        it=filter(_not_divisible(i),it)

for i in prime(1000):
    print(i)


#sorted

print(sorted(['bob','Zout',"This"],key=str.lower,reverse=True))#按照小写字母，逆向排序

def count():
    fs=[]
    for i in range(4):
        def f():
            return i*i
        fs.append(f)
    return fs

for i in range(4):
    print(i)

f1,f2,f3,f4=count()
print(f1(),f2(),f3())
print(f1.__name__)

def log(func):
    def wrac(*argc,**kw):
        print(func.__name__)
        return func(*argc,**kw)
    return wrac
#decorator 就是一个返回函数的高阶函数，其实就是想对原函数左一些增强，原函数作为返回函数的高阶函数再写一个高阶函数
@log
def now(n):
    print('133',n)
print(now(10))#现在的now函数已经是更改后的wrac，就是说原来的now做为参数传给了log
print(now.__name__)#这时候的名字就是wrac，这首加一个functools.wraps(func)就能自动吧函数名换过来了。


import functools
def log(func):
    @functools.wraps(func)
    def wrac(*argc,**kw):
        print(func.__name__)
        return func(*argc,**kw)
    return wrac

@log
def now(n):
    print('1222',n)

print(now(10))

def log(func):
    def wrac(*args,**kw):
        print('begin call')
        func(*args,**kw)
        print('end call')
    return wrac


@log
def now(n):
    print('1,23',n)

now(12)
