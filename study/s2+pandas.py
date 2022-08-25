import chardet
import pandas as pd
import numpy as np


my_data = [100,200,300,400]
np_arr = np.array(my_data)
a = pd.Series(np_arr)
print(a)

my_dice = {'a':1,'b':2,'c':3}
print(pd.Series(my_dice))

print(a[0])

import pandas as pd
import numpy as np
df = {"Name": pd.Series(['a', 'b', 'c'], index=['0','1','2']),"Age" : pd.Series(['1','2','3'], index = ['0','1','2'])}
pd.DataFrame(df)
print(df)

df['Year'] = pd.Series(['2016','2017','2018'],[0,1,2])
pd.DataFrame(df)
print(df)

a = df[0]
print(a)

#-------------------------------#

class Student(object):
    pass


s =Student()
s.name =' M '
print(s.name)

def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(set_age)



Student.set_score = set_score

s2.set_score(20)
s2.score


class Student(object):
    __slots__ = ('name.',age)

s = Student()
s,name ='M'
s.age = 20
s.score = 111
#--------------------------








import pandas as pd
df = pd.DataFrame({'Name': pd.Series(['A', 'B', 'C'] , index = ['a', 'b', 'c']),
                   'Age': pd.Series(['20', '11', '2'], index = ['a', 'b', 'c']),
                   'Nationality': pd.Series(['US', 'CHINA', 'E'], index = ['a', 'b', 'c'])
                   })


# 插入新的标签+内容
df['Year'] = pd.Series(['2020','2011','2031'], index = ['a','b','c'])
print(df)
# 列表合成
df['birth'] = df['Year'] + df['Age']

# 检索
print(a.loc[['a','b'],['Name','Age','birth']])
 
# 删除列  axis=0 删除行
a.drop('birth',axis = 1)

import  pandas as pd
import numpy as np

# random.randn 标准正态分布
df1 = pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
# 条件判断
a1 = df1[(df1['Z']> 0 ) & (df1['X']>1)]
print(a1)
# 重置index  默认0开头
df1.reset_index()

df1['ID'] = ['a','b','c','d','e']
df1.set_index('Z')

#生成多级索引对象
outside =['0LEVEL','0LEVEL','0LEVEL','ALEVEL','ALEVEL','ALEVEL']
inside  =[21,21,32,12,11]
my_index = list(zip(outside,inside))
print(my_index)

my_index =  pd.MultiIndex.from_tuples(my_index)
print( my_index)
#多级索引转化为DataFrame
df = pd.DataFrame(np.random.randn(5,2),index = my_index , columns= ['A','B'])
print(df)

df.index.names = ['levels' , 'name']

df.xs(21,level= 1)

#----------------------------------------------#
outside1 = ['GOOD','GOOD','BAD','BAD','BAD','BAD']
inside1  = ['A','B','C','D','E','F']
my_list  = list(zip(outside1,inside1))
my_list = pd.MultiIndex.from_tuples(my_list)
print(my_list)
df1  =  pd.DataFrame(np.random.randn(6,2),index = my_list ,columns= [1,2])
print(df)

a = df1.loc['GOOD'].loc['A']
print(a)

#添加index
df1.index.names = ['levels','name']
print(df1)
print(df1.xs('A',level=1))
#------------------------------
df2 = {'A': [1, np.nan, 3], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9] } #np.nan添加None值
df2 =pd.DataFrame(df2)

b = df2.dropna()#删除None值
a = df2.fillna(1)#修改替换None值
print(a)

df3 = {'COMPANY':['BAIDU','BAIDU','OKAI','OKAI','TMAIL','TMAIL'],
'PERSON':['A','B','C','D','E','F'],'SAIL':[200,100,300,200,330,300]}

df3 = pd.DataFrame(df3)
print(df3)

print(df3.groupby('COMPANY').mean())  #.mean()求每组平均值
print(df3.groupby('COMPANY').count()) #.count()计数
print(df3.groupby('COMPANY').describe()) #计数、平均数、标准差、最小值、25% 50% 75% 位置的值、最大值
print(df3.groupby('COMPANY').describe().transpose()) #竖版

print(df3.groupby('COMPANY').describe().transpose()['BAIDU'])
#---------------------------------
#堆叠

d = {'A':[1,2,3,4,5,6,7],'B':[1,2,3,4,5,6,7],'C':[1,2,3,4,5,6,7]}
d2 = {'A':[1,2,3,4,5,6,7],'B':[1,2,3,4,5,6,7],'C':[1,2,3,4,5,6,7]}
d3 = {'A':[1,2,3,4,5,6,7],'B':[1,2,3,4,5,6,7],'C':[1,2,3,4,5,6,7]}
d=pd.DataFrame(d)
d2=pd.DataFrame(d2)
d3=pd.DataFrame(d3)

d4 = pd.concat([d,d2,d3],axis=1)
d4.index.names = ['num']
print(d4)
print(d4.loc[0].loc['A'])

#--------------------------------------
#归并
#.merge()
left = pd.DataFrame({'Key':['K1','K2','K3'],'A':['A1','A2','A3'],'B':['B1','B2','B3']})
right = pd.DataFrame({'Key':['K0','K2','K3'],'C':['C1','C2','C3'],'D':['D1','D2','D3']})

print(pd.merge(left,right,how = 'outer',on ='Key'))  #inner交集，Outer并集

#.join()
left1 = pd.DataFrame({'A':['A1','A2','A3'],'B':['B1','B2','B3']},index =['K1','K2','K3'])
right1 = pd.DataFrame({'C':['C1','C2','C3'],'D':['D1','D2','D3']},index =['K0','K2','K3'],)
left1.index.names = ['left1']
right1.index.names = ['right1']
print(right1)
print(left1)
print(left1.join(right1))
print(left1.join(right1,how ='outer'))
#------------------------------------------------

df4 = pd.DataFrame({'A':[1,2,3,4],'B':[44,333,44,11],'C':['a','b','c','d']})
print(df4)

a = df4['B'].unique()#获取不重复的值
print(df4['B'].nunique())#不重复值个数
print(a)
print(df4['B'].value_counts())#获取不重复的值和个数
#-----------------------------

def square(x):
    return x*x
print(df4['A'].apply(square))
print(df4['A'].apply(lambda x:x+x))

#-----------------------------------------------
print(df4)
print(df4.columns)
print(df4.index)


#-----------------------------------------------
#排序 .sort()

print(df4.sort_values('B'))

print(df4.isnull())  #查找None

#——------------------------------
import pandas as pd
data = pd.DataFrame({'animal':['dog','dog','dog','CAT','CAT','CAT'],'colour':['white','black','white','white','yellow','black']
                     ,'C':['x','y','x','y','x','y'],'Age':[3,2,1,3,4,5]})
print(data)
print(pd.pivot_table(data,values='Age',index=['animal','colour'],columns=['C']))

data.to_csv("animal.csv",index=False)
pd.read_csv("animal.csv")

data.to_excel("animal.xlsx",sheet_name="sheet1")
pd.read_excel('animal.xlsx',sheet_name = 'sheet1')

df5 = pd.read_html('https://en.wikipedia.org/wiki/Udacity')
df5[1]



#------
import os

a =  os.path.split("C:/Users/Administrator/Desktop/hem2.json")
print(a)    #os.path.split（)拆分路径和文件名

os.mkdir('/Users/Administrator/Desktop/111')  #指定路径创建新目录
os.rmdir('/Users/Administrator/Desktop/111')   #指定路径删除目录
os.rename('animal.xlsx','animal1.xlsx')  #重命名

with open('a.txt','w') as f:
    f.write('H')

with open('a.txt','r') as y:
    print(y.read())

#--------
import json
a = dict(name='a',age=12,score = 1)
b= json.dumps(a)
print(b)

json.loads(b)

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
#-----------------

import  os

print('Process (%s) start...' % os.getpid())
pid = os.fork()

if pid == 0:
    print('I am child process (%s) and my parent is %s.',os.getpid(),os.getppid())
else:
    print('I (%s) just created a child process (%s).',os.getpid(),pid)    #mac/linux上可运行


import os
from multiprocessing import Process

pid =os.getpid()
print(pid)
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')




from collections import namedtuple      #定义数据类型
point = namedtuple('point',['x','y'])
p = point(1,2)


from collections import deque  #list插入数据
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')


from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+ 1



import struct
print(struct.pack('>I',10240099))


#------------------------------------图片处理
from PIL import Image,ImageFilter
picture = Image.open('C:\\Users\\Administrator\\Desktop\\annotations.png')
w, h =picture.size

picture.thumbnail((w//2,h//2))  #picture 缩放50%
picture.save('./thumbnail.png','png')

picture2 = picture.filter(ImageFilter.BLUR)
picture2.save('filter.png','png')    #应用图片模糊滤镜

#验证码生成
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import  random
#随机字母
def suijizimu():
    return chr(random.randint(60,90))

#随机颜色1
def suijicolor():
    return (random.randint(64,255), random.randint(64,233), random.randint(64,255))

#随机颜色2
def suijicolor2():
    return (random.randint(32,127), random.randint(32,127),random. randint(32,127))

width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('arial.ttf',36)
draw = ImageDraw.Draw(image)

#像素填充
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=suijicolor())
#输出文字
for t in range(4):
    draw.text((60 * t + 10,10), suijizimu(), font = font , fill = suijicolor2())

image = image.filter(ImageFilter.BLUR)
image.save('yanzhengma.jpg','jpeg')

#-----------------------------------------------检测编码
import chardet
print(chardet.detect(b'HEllo!'))
data = '一二三四五'.encode('gbk')
print(chardet.detect(data))

#----------------------------------------------------  GUI
from tkinter import *
import tkinter.messagebox as mb

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput =Entry(self)
        self.nameInput.pack()
        self.alerButton = Button(self, text='Hello', command =self.user)
        self.alerButton.pack()
    def user(self):
        name = self.nameInput.get() or 'world'
        mb.showinfo('Message','Hello,%s'% name)
app =Application()
app.master.title('hello!')
app.mainloop()

#-------------------------------------------------

print('Content-type:text/html')
print()
print('<html>')
print('<head>')
print('<meta charset = "utf-8">')
print('<title>Hello Word - my first GGI</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word!i m GGI</h2>')
print('</body>')
print('</html>')

#------------------------------------------------------

#实例
num1 = input(':')
num2 = input(':')
sum =float(num1)+float(num2)
print(sum)
#---

sum = float(input('please input:'))**0.5
print(sum)

#----------------------------------------------------

import numpy as np
a = [[1,2,3],[1,2,3]]
npa =np.array(a)   #堆叠

b = np.array([1,2,3,4,5,6,7,8])
b1 = b.reshape(2,4)    #数组拆分

np.sqrt(b1)  #求开方
np.exp(b1)    #求e次幂

#-----------------------------------------------------

def f(a,b,*,c):
    return a+b+c
f(1,2,c = 3)


def f(a,b,/,c,d,*,e,f):  #a，b必须用位置参数，/可使用位置参数or关键字参数  *必须用关键字参数
    print(a,b,c,d,e,f)
f(1,2,3,d=4,e=5,f=6)


[str(round(355/113,i))for i in range(1,3)]



import  FIbo
dir(FIbo)

FIbo.fib(500)


for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end = ' ')
    print('立方:',repr(x*x*x).rjust(4))

table = {'Goolge': 1,'Runoob': 2,'Taobao': 3}
print('Runoob:{0[Runoob]:d};Goolge:{0[Goolge]:d};Taobao:{0[Taobao]:d}'.format((table)))

with open('test1','w') as f:
    f.write('hello')
#------------------------------------------
#pickle
import pickle


data = {'a':[1,2,2,3,4+6j],
        'b':('string',u'Unicode string'),
        'c':None}

list = [1,2,3]
list.append(list)

output = open('data.pkl','wb')

pickle.dump(data,output)
pickle.dump(list,output,-1)

#pickle
import pprint,pickle

pkl_file = open('data.pkl','rb')

data = pickle.load(pkl_file)
pprint.pprint(data)

data1 = pickle.load(pkl_file)
pprint.pprint(data1)
pkl_file.close()

class Myclass:
    i =12345
    def f(self):
        return 'hello'

def __init__(self):
    self.data= []


class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i =imagpart

x = Complex(3.0,-4.5)
print(x.r,x.i)

class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('{},{}'.format(self.name,self.age))


import mysql.connector

mydb = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '123456',
    database = 'runoob_db',
    auth_plugin='mysql_native_password'

)
#print(mydb)
mydb.commit()
a = mydb.cursor()

sql = 'create table fav (id int auto_increment primary key,name varchar(255),fav varchar(255))'
a.execute(sql)

sql = ' insert into fav(id,name)values(%s,%s)'
val = [
    (155,'fff'),
    (145,'sss'),
    (167,'lll')
    ]
a.executemany(sql,val)



sql1 = 'SELECT  users.name AS user fav1.name AS favorite FROM users INNER JOIN fav1 ON users.fav = fav1.id' #join 组合表
a.execute(sql)
myresult = a.fetchall()

#a.execute('ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')  #创建主键

#--------------------------------------------------inset
'''sql = 'INSERT INTO customers(name,address)VALUES(%s,%s)'
val = ('sss','abdj 2')
a.execute(sql,val)
mydb.commit()
print(a.rowcount,'record inserted,ID:',a.lastrowid)'''
#---------------------------------------------------
sql = "SELECT * FROM customers WHERE address = %s"
adr = ('Green Grass 1',)
a.execute(sql,adr)

#sql = "SELECT * FROM customers WHERE address like '%way%'"
#a.execute(sql)
#a.execute('SELECT * FROM customers')
#myresult1 = a.fetchone()
myresult = a.fetchall()
for x in myresult:
    print(x)
'''
sql = ' select * from customers order by id'  #排序  (降序DESC)
sql = ' delete from customers where address = ' '  #删除
sql =' drop table customers'#删表
sql = ' drop table if exists customers' #只在表存在时删除
sql = "update customers set address = 'Canyon 123' where arrress = 'Valley 345'" #更新表 修改内容
'''
a.execute('select * from customers limit 5')  #筛选前五条
a.execute('select * from customers limit 5  offset 2') #从第二条开始返回五条
myresult = a.fetchall()
for x in myresult:
    print(x)

#a.execute('SHOW DATABASES')

a.execute('SHOW TABLES')
a.execute('CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))')
mycusor.execute('ALTER TABLE sites ADD COLUMN id int AUTO_INCREMENT PRIMARY KEY')

#join
sql = 'select customers.address as user,users.name as favorite' \
      'from users inner join users on customers.address=users.name'
a.execute(sql)
myresult = a.fetchall()



#--------------------------------------------
def digui(x):
    if x>0:
        result = x + digui(x-1)

    else:
        result = 0
    return result

print(digui(6))


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class mynumbers:
    def __iter__(self):
        self.a =1
        return self

    def __next__(self):
        if self.a <= 20:

            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = mynumbers()
myiter = iter(myclass)

print(next(myiter))

list = []
for i in range(10):
    list.append(i)
print(list)


import  numpy as pd
#这是一个numpy过滤器
arr = np.array([1,2,3,4,5])

filter_arr = []
def Filter(x):
    for x in arr:
        if x >2:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

    newarr = arr[filter_arr]
    print(newarr)
#直接过滤
filter_arr1 = arr >2
newarr = arr[filter_arr1]


value = float(input())
unit  = input('请输入单位:')
if unit == 'in' or unit =='英寸':
    print('%f英寸=%fcm'%(value,value * 2.54))
elif unit =='cm' or unit =='厘米':
    print('%f厘米 = %fin'%(value,value/2.54))

num = int(input('输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end+1 ):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d是素数'% num)

def lifang(x):
    return x * x * x

num = int(input())
r = 0
while num>0:
    r = r * 10 + num % 10
    num//10

print(r)


for i in range(1,20):
    for x in range(1,33):
        z= 100 -x -i
        if i*5+x*3+z/3 == 100:
            print("%d,%d,%d"%(i,x,z))
m

import random



m = 1000
for i in range(0,100):
        print('game begin \nm:%d' % m)
        print('-'*20)
        m = m-200
        if m <= 0:
            print('Insufficient balance')
            break
        i = i+1
        print('第%d轮'%i)
        x1 = random.randint(1, 6) + random.randint(1, 6)
        print(x1)
        if i > 1:
            continue
        else:
            if x1 ==7 or x1==11:
                print('win')
                m = m + 200
                break
            elif x1==2  or x1==3 or x1==12:
                print('lose')
                m = m - 200
                break
            x2 = random.randint(1, 6) + random.randint(1, 6)
            if x2 == x1:
                print('win')
                m = m + 200
            elif x2 ==7:
                print('lose')
                m = m - 200

a,b =0,1
for x in range(1,20):
    x = x +1
    while b<x:
        a,b = b,a+b
        print(b)

import  math

for num in range(1,10000):
    result = 0
    for f in range(1,int(math.sqrt(num))+1):
        if num % f == 0:
            result = result+f
            if f >1 and num//f != f:
                result = result + num//f
    if result ==num:
        print(num)



def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def gcb1(x1,y1):
    if x1 > y1:
        smaller = y1
    else:
        smaller = x1

    for i in range(1,smaller+1):
        if (y1 % i == 0) and (x1 % i == 0):
                h = i
    return h


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

#回文判断
def huiwen(x, num1=0):
    y = x
    while x >0:
        num1 = num1 *10 + x %10
        x =x // 10

    if y == num1:
        print('true')
    else:
        print('false')

    print('num:%d\nresult:%d' % (y, num1))

#素数判断
def sushu(x):

    if x >2:
        for i in (2,x-1):
        if x %  i == 0:
            print('False')
        else:
            print('true')
    elif x == 2:
        print('true')
    else:print('false')



import os
import time


#跑马灯
def run():
    words = 'AAAAAAAAAAAAAAABBBB..'
    while True:
        #清理屏幕
        os.system('clear')
        print(words)
        time.sleep(0.2)
        words = words[1:]+words[0]

#验证码生成
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
def YZM():
    def yzm(len1 = 4):
        all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        l = len(all_chars)-1
        global code
        code =''
        for i  in range(len1):
            index = random.randint(0,l)

            code = code +all_chars[index]
        return code


    #随机颜色1
    def suijicolor():
        return (random.randint(64,255), random.randint(64,233), random.randint(64,255))

    #随机颜色2
    def suijicolor2():
        return (random.randint(32,127), random.randint(32,127),random. randint(32,127))

    width = 60 *2
    height = 60
    image = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('arial.ttf',36)
    draw = ImageDraw.Draw(image)

    #像素填充
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=suijicolor())
    #输出文字

    draw.text((10 ,10), yzm(), font = font , fill = suijicolor2())
    print(code)
    image = image.filter(ImageFilter.BLUR)
    image.save('yanzhengma.jpg','jpeg')

#-------------------------------------------------------------------------------

def getname(filename,has_dot = False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename)-1:
        index = pos

        return filename[index:]
    else:
        return ''

#返回max和第二大的值
def max1(x):
    if x[0]>x[1]:
        m1 = x[0]
        m2 = x[1]
    elif x[0]<x[1]:
        m1 = x[1]
        m2 = x[0]
    for index in range(2,len(x)):
        if x[index] > m1:
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1,m2


def min1(x):
    '返回min和第二小的值'
    if x[0]<x[1]:
        m1 = x[0]
        m2 = x[1]

    elif x[0]>x[1]:
        m1 = x[1]
        m2 = x[0]
    for index in range(2,len(x)):
        if x[index] < m1:
            m1 = x[index]
        if x[index]  <m2  :
            m2 = x[index]

    return m1,m2
#——————————————————FALSE(该函数只能求最小值）

def yearday(year):
    ' leap year true or false'
    return year % 4 ==0 and year % 100 !=0 or year %400 ==0
def which_day(year,month,date):
    days_of_month = [[30,28,31,30,31,30,31,31,30,31,30,31],
                     [30,29,31,30,31,30,31,31,30,31,30,31]][yearday(year)]
    total = 0
    for index in range(month-1):
        total = total+days_of_month[index]
    'count total days'
    return total+date
#————————————————————————————————————————————

def main():
    'double color ball'
    if __name__ == '__main__':
        main()

    def display(balls):
        for index, ball in enumerate(balls):
            if index == len(balls)-1:
                print('|',end ='')
            print('%02d'%ball,end = ' ')
        print()

    def random_select():
        red_balls = [x for x in range(1,32)]
        select_balls = []
        select_balls = sample(red_balls,6)
        select_balls.sort()
        select_balls.append(randint(1,16))
        return select_balls

    n = int(input())
    for i in range(n):
        display(random_select()

#约瑟夫环
def main():
    persons= [True]*30
    counter,index,number = 0,0,0
    while  counter <15:
      #  if persons[index] :
        number += 1
        if number == 9:
            persons[index] = False
            counter += 1
            number = 0
        index +=   1
        index = index % 30

    for person in persons:

        print('ji'if person ==True else 'fei',end= ',')
    '''   if person ==True:
            print('j')
        else :
            print('f')'''

if __name__ == 'main':
    main()

import os

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn ='x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter <9:
            move = input('%s'% turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn =='x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice= input('again? yes/no')
        begin = choice == 'yes'

if __name__ == '__mian__':
    main()

#————————————————————————————————————————————————————
#————————————————————————————————————————————————————
class s(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,course_name):
        print('%s is studying %s'%(self.name,course_name))

def main():
        # 创建学生对象并指定姓名和年龄
        stu1 = s('l', 38)
        # 给对象发study消息
        stu1.study('Python程序设计')

        stu2 = s('w', 15)
        stu2.study('思想品德')


if __name__ == '__main__':
        main()


class Test:
    def __init__(self):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    test.__bar()
    print(test.__foo)

if __name__ == 'main':
    main()

#————————————————————————————————————————————————
'show time'
class clock(object):
    def __init__(self,hour =0,minute =0, second =0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second +=1
        if self.second == 60:
            self.minute += 1
            self.hour = 0
            if self.minute == 60:
                self.minute =0
                self.hour += 1
                if self.hour == 24:
                    self.hour =0


    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)

    def show(self):
        return 'now time is %dh%dmin%ds'%(self.hour,self.minute,self.second)



def main():
    a = int(T1()[0])
    b = int(T1()[1])
    c = int(T1()[2])
    C=clock(a,b,c)
    print(C.show())

def main1():
    C=clock.now()
    print(C.show())

def T():
    '''time now'''

    localtime = time.asctime(time.localtime(time.time()))
    times = localtime.split()[3]
    times = times.replace(':', '')
    list = []
    for i in times:
        list.append(i)
    SS = 0
    t = []
    test1 = list[SS] + list[1 + SS]
    t.append(test1)
    for x in range(2, 5, 2):
        test = list[x] + list[1 + x]

        t.append(test)
    return t

def T1():
    localtime1 = localtime(time())
    return (localtime1.tm_hour,localtime1.tm_min,localtime1.tm_sec)
#——————————————————————————————————————————————

class Person(object):
    """solts限定对象"""
    __slots__ = ('_name','_age','_gender')
    def __init__(self,name,age):
        self._name= name
        self._age = age

    #访问器
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    #修改器
    @name.setter
    def name(self,name):
        self._name =name

    def r(self):
        print('name is %s,age is %d'%(self._name,self._age))

def main():
    person=Person('a',12)
    person.r()
    person.name = 'q'
    person.r()



from math import sqrt

class sanjiaoxing(object):
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self.c = c

    def is_true(self):
        return  a+b>c and b+c >a and c+a >b

    def perimeter(self):
        return self._a+self._b+self._c

    def area(self):
        half = self.perimeter()/2
        return sqrt(half*(half-self._a))*(half-self._b)*(half-self._c)


def main():




class student(object):
    def get_socre(self):
        return self.score





from abc import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object,metaclass=ABCMeta):

    def __init__(self,name,hp):
        self._name =name
        self._hp =hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        if hp > 0:
            self._hp = hp
        else:
            self._hp = 0

    @property
    def alive(self):
        return self._hp >0

    @abstractmethod
    def attack(self,other):
        pass


class ultraman(Fighter):

    _solts_ =('name','_hp','_mp')
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp =mp

    def attack(self,other):
        other. hp = random.randint(15,25)

    def hug_attack(self,other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp *3//4
            if  injury >= 50:
                injury  = injury
            else:
                injury =50
            return True

        else:
            self.attack(other)
            return False


    def magic_attack(self,others):

        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10,15)
            return True
        else:
            return False

    def hpreturn(self):
        returnHP = randint(5,10)
        self._mp += returnHP
        return returnHP

    def __str__(self):
        return 'people:%s has hp:%d has mp:%d'%(self._name,self._hp,self._mp)


class   Bad(Fighter):
    __slots__ = ('_name','_hp')
    def __init__(self,name,hp):
        super().__init__(name, hp)
        self._i = 0
    def attack(self,other):
        other.hp -= randint(10,20)

    def __str__(self):
        return 'bad name:%s hp:%d\n'%(self._name,self._hp)
    def next(self):
        if self._i == 0:
            self._i +=1
            return self._name
        elif self._i ==1:
            self._i += 1
            return self._hp
        else:
            raise StopIteration()

def is_any_alive(mosters):
    for moster in mosters:
        if moster.alive > 0:
            return True
    return False

def choseone(mosters):
    mosters_len = len(mosters)
    index =randrange(mosters_len)
    moster = mosters[index]
    if moster.alive > 0:
        return moster

def show_message(ultraman,mosters):
    print(ultraman)
    for moster in mosters:
        print(moster,end ='')



def main():
    u = ultraman('dijia',1000,120)
    b4 =Bad('gesila',500)
    b2 = Bad('baigujing',100)
    b3 = Bad('niumowang',750)
    m1 = [b3,b2,b4]
    fight_round = 1
    while u.alive>0 and is_any_alive(m1):
        print('\n======%d round===========\n'%fight_round)
        m =choseone(m1) #选中
        skill = randint(1,10) #随机选择attack way
        if skill <= 6:
            print('%s attack %s'%(u.name,m.name))
            u.attack(m)
            print('%s  magic huilan %d'%(u.name,u.hpreturn()))
        elif skill <= 9:
            if u.magic_attack(m):
                print('%s use magic'%u.name)
            else:
                print('magic use fail')
        else:
            if u.hug_attack(m):
                print('%s use huge magic attack %s'%(u.name,m.name))
            else:
                print('%sattack%s'%(u.name,m.name))
                print('%smagic%d' % (u.name, u.hpreturn()))
        if m.alive > 0:
            print('%s counterattack %s'%(m.name,u.name))
            m.attack(u)
        show_message(u,m1)
        fight_round += 1
    print('\n======over=======\n')
    if u.alive >0:
        print('%swin'%u.name)
    else:
        print('moster win')

if __name__ =='__main__':
    main()


#扑克
class Card(object):
    def __init__(self,suite,face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite
    @property
    def face(self):
        return self._face
    def __str__(self):
        if self._face == 1:
            face_str ='A'
        elif self._face == 11:
            face_str ='J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s'%(self._suite,face_str)

    def __repr__(self):
        return self.__str__()

class Poker(object):
    def __init__(self):
        self._cards = [Card(suite,face)
                      for suite in '♠♥♣♦'
                      for  face in range(1,14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards
    def shuffle(self):
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        card = self._cards[self._current]
        self._current += 1
        return card

    def has_card(self):
        return self._current <len(self._cards)



class Player(object):
    def __init__(self,name):
        self._name =name
        self._cards_had_on = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on(self):
        return self._cards_had_on

    def get_cards(self,card):
        self._cards_had_on.append(card)
    def card_sort(self,card_key):
        self._cards_had_on.sort(key = card_key)

def get_key(card):
    return (card.suite,card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('a'), Player('b'), Player('c'), Player('d')]
    for i in range(1,13):
        for player in players:
            player.get_cards(p.next)
    for player in players:
        print(player.name +':',end = ' ')
        player.card_sort(get_key)
        print(player.cards_on)

if __name__ == '__main__':
    main()


from abc import ABCMeta,abstractmethod
class Employee(object,metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 15000.0
class Programmer(Employee):
    def __init__(self,name,workingtime = 0):
        super().__init__(name)
        self._workingtime =workingtime
    @property
    def workingtime(self):
        return self._workingtime
    @workingtime.setter
    def workingtime(self,workingtime):
        if self._workingtime > 0:
            self._workingtime = workingtime
        else:
            self._workingtime = 0
    def get_salary(self):
        return 150.0 * self._workingtime
class Saler(Employee):
    def __init__(self,name,sales = 0):
        super().__init__(name)
        self._sales =  sales
    @property
    def sales(self):
        return self._sales
    @sales.setter
    def sales(self,sales):
        if self._sales > 0:
            self._sales = sales
        else:
            self._sales =  0
    def get_salary(self):
        return 1200.0 +  self._sales * 0.05

def main():
    emps = [
        Manager('A'), Programmer('a'),
        Manager('B'), Saler('e'),
        Saler('f'), Programmer('b'),
        Programmer('c')
    ]
    for i in emps:
        if isinstance(i,Programmer):
            i.workingtime_setter=int(input('please input %s  work time:'%i.name))
        elif isinstance(i,Saler):
            i.sales = float(input('please input %s saled money:'%i.name))

        print('%s  money:%s'%(i.name,i.get_salary()))




list = (['a','b','c','d','a','a'])
list2 = set(['a','f'])
freelist = []
for i in list:
    if list.count(i) == 1:
        if i not in freelist:
            freelist.append(i)


freelist = set([i for i in list if list.count(i) > 1])

print(input(list2.intersection(list))) #交集
print(input(list2.difference(list)))  #差集


#装饰器
def a_new_decorator(a_func):

    def wrapTheFunction():
        print('doing something before excuting a_func()')
        a_func()
        print('doing something after excuting a_func()')

    return wrapTheFunction
@a_new_decorator
def a_function_requiring_decoration():
    print('i am the function which needs some decoretion to remove mt foul smell')

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)


def hi():
    return 'hello'

def returnhi(func):
    print('i am hi()')
    print(func())

def add_to(num,target= []):
    target.append(num)
    return target


import numpy as np
test1 = np.array([1,2,34,22])
test2 = np.array([2.1,5.3,1.1,2.1])

test1 = np.expand_dims(test1,0)  #增加维度


a = np.array([1,2,3,4,5,6])
a_2d = a[np.newaxis,:] #增加维度
a_none = a[:,None]#增加维度
a_expand = np.expand_dims(a,axis=1)#增加维度
s_squeeze = np.squeeze(a_expand)#减少维度
a_squeeze_axis = a_expand.squeeze(axis=1)

a1 = a.reshape([2,3]) #改变维度和尺寸
a2 = a.reshape([3,1,2])

aT1 = a1.T  #矩阵转置
aT2 = np.transpose(a1)

feature_a = np.array([1,2,3,4,5,6])
feature_b = np.array([11,22,33,44,55,66])
c_stack = np.column_stack([feature_a,feature_b])    #列合并


sample_a = np.array([0,1.1])
sample_b = np.array([1,2.2])
c_stack1 = np.row_stack([sample_a,sample_b])  #sample合并
c_stack1 = np.hstack([sample_a,sample_b])  #vstack
c_stack1 = np.vstack([sample_a,sample_b]) #hstack


a = np.array([
[1,2],
[3,4]
])
b = np.array([
[5,6],
[7,8]
])

print(np.concatenate([a, b], axis=0))
print(np.concatenate([a, b], axis=1))

a = np.array(
[[ 1, 11, 2, 22],
 [ 3, 33, 4, 44],
 [ 5, 55, 6, 66],
 [ 7, 77, 8, 88]]
)
a1 = np.vsplit(a,indices_or_sections=2) #分成两段
a2 = np.vsplit(a,indices_or_sections=[2,3])#0-2,2-3,3+

print(np.split(a, indices_or_sections=2, axis=0))  # 分成两段
print(np.split(a, indices_or_sections=[2,3], axis=1))  # 在第二维度， 0~2 一段，2~3 一段，3~一段


import random
import time

def download(filename):
    print(f'begin download...{filename}')
    time.sleep(random.randint(2,6))
    print(f'{filename}download success')


def upload(filename):
    print(f'begin upload{filename}...')
    time.sleep(random.randint(2,6))
    print(f'{filename}upload success')

start = time.time()
download('aaa')
end = time.time()
print(f'use time:{end - start:.2f}s')


def record_time(func):
    def wrapper(*args,**kwargs):
        s  = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.3f}s')
        return result
    return wrapper

download = record_time(download)  

