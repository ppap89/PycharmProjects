'''def power(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    print(s)

power(5,2)'''

'''def s(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

s('M',20)'''
#递归  阶乘计算
'''def fact(n):
  if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))
'''

''''def move(n, a, b, c): #汉诺塔
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)


move(3, 'A', 'B', 'C')'''

'''L=[]
n = 1
while n < 10:
    L.append(n)
    n = n+2

print(L)
'''

'''L = list(range(100))
print(L[:10:2])'''

def trim(s):
    while s[:1] == ' ':
        s = s[1:]
        print(s)
    while s[-1:] == ' ':
        s = s[:-1]
        print(s)
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


a = {'a':1,'b':2,'c':3}
for k,v in a.items():
    print (k,v)

a = {'a': '1', 'b': '2', 'c': '3'}
[print(k+'='+ v) for k , v in a.items()]

def findMinAndMax(L):
    if L == 0:
        return None,None
    elif:
        min = L[0]
        max = L[0]
        for v in L:
            if v > L[0]:
                max == v
            if v < L[0]:
                min == v
        return max,min
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


g = (x + 1 for x in range(10))
for i in g:
    print(next(g))

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'

print(fib(6))

#-------------------------------------------------------------------#
#map/reduce  map(函数,数据) reduce(）求和

def add(x,y,f):
    return f(x) +f(y)

print(add(-1,-1,abs))


def f(x):
    return abs(x)

r = map(f,[-1,1,-2,4,-5])
print(list(r))

from functools import reduce
def f(x,y):
    return x*10+y
def p(s):
    a = {'1':1,'2':2,'3':3}
    return a[s]

print(reduce(f,map(p,'123')))

def normalize(name):
    name = name.lower()
    name = name.capitalize()
    return name

print(list((map(normalize,['adam', 'LISA', 'barT']))))

from functools import reduce
def prod(L):

    def f(x,y):
        return x * y
    return reduce(f,L)

s=(prod([3,5,7,9]))
print(s)


def str2float(s):
        def a(x,y):
            return x*10+y
    n = s.index('.')
    return  reduce(a,map(int,s[:n]))+reduce(a,map(int,s[n+1:]))

from functools import reduce
def a(x,y):
    return x * 10 + y

def str2float(s):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    flag = s.index('.')
    s1,s2= s[:flag],s[flag+1:]
    def char2num(s):
        return d[s]

    c = list(map(char2num,s1))
    v = list(map(char2num,s2))
    return reduce(a,c)+reduce(a,v)/(10**len(v))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
#----------------------------------------------------------#
#filter（） 筛选

def odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def not_divisible(n):
    return lambda x:x%n >0
def primes():
    yield 2
    i =odd_iter()
    while True:
        n = next(i)
        yield n
        i = filter(not_divisible(n),i)

for n in primes():
    if n<1000:
        print(n)
    else:
        break


def is_palindrome(n):

    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')



#-----------------------------------------------------------#
#sorted() 排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

s = sorted(L,key=by_name)
print(s)

1

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return -t[1]

s = sorted(L, key=by_score)
print(s)

#-----------------------------------------------------------#
def sum(*args):
    def l_sum():
        s = 0
        for n in args:
            print(n)
            s = s+n
        return s
    return l_sum

f  = sum(3,1)
print(f)

f()



L = list(filter(lambda n: n %2 == 1 ,range(1,20)))
print(L)

def now():
    print('1')

f =now
f()

now.__name__

#----------------------------------------------------#
#class


class student(object):
    def __init__(self,name,score):
        self.__name = name   #无法从外部访问
        self.__score = score  #无法从外部访问
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
    #从外部访问
    def  get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        self.__name = name



b = student('B',50)
b.set_name('C')
print(b.get_name())


#----------------------------------------------------
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender

bart = Student('Bart', 'male')

if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
#------------------------------------------
#子类父类
class Animal(object):
    def run(self):
        print('runing')

class Dog(Animal):
    pass
class Cat(Animal):
    pass

Cat().run()

#-----------------------------------------------
obj = Student
hasattr(obj,'name')

setattr(obj,'y',1)
getattr(obj,'y')
obj.y
#-----------------------------------------------------
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
#-------------------------------------------------
class STUDENT(object):
    pass

def set_score(self,score):
    self.score = score

s =STUDENT()
STUDENT.set_score = set_score

s.set_score(10)
print(s.score)

#------------------------------------------
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('must be an interger')
        if value < 0 or value > 100:
            raise ValueError('must between 0~100')
        self._score = value

s= Student()
s.set_score(60)
s.get_score()

#-------------
class animal(object):
    pass

class runable(object):
    def run(self):
        print('running')
class flyable(object):
    def fly(self):
        print('flying')



class mammal(animal):
    pass
class bird(animal):
    pass
class dog(mammal,runable):
    pass
class bat(mammal,flyable):
    pass


a= dog()
print(a)
class parrot(bird):
    pass
class ostrich(bird):
    pass


#---------------------------------
import random
list = []
for i in range(0,5):
    s = random.randint(0,5)

    list.append(s)
print(list)

import os
with open("douban.txt","w") as f:

    f.write('这是个测试')


with open('douban.txt','r')as f:


    for line in f.readline():
        print(line)

f.open('Users\\Administrator\\Desktop\\2021060201-1.jpg','rb')#rb模式打开图片视频等二进制文件
f.read()

f.open('GBK.txt','r',encoding=gbk) #读取读取GBK编码文件
f.read()

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())   #getvalue()获取写入的str

import os
a = os.name
print(a)
#------------------------------
import os
a =  os.getcwd()
os.chdir('./')
