# his my learning of python
# 2017.3.15
我感觉要是不花更多的时间，更加努力，我的学习就要到头了。

## 在atom中文输出python3解决办法  
'''
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
'''
## map,reduce ,filter

## 返回函数返回的是函数，这个函数还没有执行，但是参数都是定了的，所以在返回函数中定义的函数不要含有后续会变化的函数，不然这个参数会一直使用

## 反正我感觉decorator 就是对一个已经有的函数做一些增强


# 下面要开始学面向对象方面的了
## 一来就有问题。双下划线开头就变成私有变量了
## 双下滑开头和结尾事特殊变量，不是私有的,
## 使用__slots__ 能够简简单单哪。只要这几个属性，你要其他属性那就错了。
'''
class Student(object):
    __slots__ = ('name', 'age')#一个元组搞定
'''
## @property 能够将一个属性封装成方法，同时，又能用访问属性的方式访问这个函数。它会自动生成一个@setter装饰器，用于设置通过函数设置属性

## __str__ 将这个类变成我们想要的输出
'''
def __str__(self):
    return 'Student is %s, and age :%d' % (self.__name, self.score)

print(Stuent('gg',11))
'''
这样就可以输出Student is gg, and age : 11， 而不是这个类的地址等等。
