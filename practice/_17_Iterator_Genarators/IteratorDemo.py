'''
EVERYTHING IS AN OBJECT IN PYTHON
'''

'''
Iterator  : Speed of execution
Generator : Memory Management 


Iterator  : Using for loop 
Generator : Generator function    --> 'yield' in function
            Generator Expression  --> Comprehension mechanism
                                          - List comprehension
                                          - Set comprehension
                                          - Dict comprehension

2.X :   range()   : Iterator 
        xrange()  : Generator

3.X :   range()   : Generator

'''
print("--------GENERATOR in 3.X-----------")
for i in range(10):
    print(i)

var = print("--------ITERATOR-----------")
list1 = [1, 2, 3, 4, 5, 6]
for each in list1:
    print("Element in list :", each)
print("End of for loop")

# 2  Steps executed when we use sequence in for loop
list1.__iter__()  # will be called only once
list1.__next__()  # will be called len of seq + 1 times

'''
In for loop :
=================
range(genrator)(3.x)   2.x ==> range(iterator),xrange(generator)  
string Iterator
list   Iterator
tuple  Iterator
byte arrays 
buffers

Iterator  --  When we require faster iteration, irrespective of memory constraints.
Generator --  When memory constraints exists.

Python 2.x
------------
range  - Iterator   -- Memory will be allocated for all 1L values
xrange - Generator  -- Memory will be created for one value at a time
                       0 - Memory X
                       1 - Memory X
                       2 - Momery

Python 3.x
------------
range - Generator

'''


l1 =[1,2,3,4,5]
print(l1.pop(4))
print(l1.insert(0,100))
print(l1)


'''
Created on 31-Mar-2020

ITERATOR :
----------
Iterator is an object which will return data, one element at a time. 
Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__() ,   collectively called the iterator protocol.
An object is called iterable if we can get an iterator from it.
'''

'''ITERATORS'''

for i in [1,2,3,4,5]:
    print(i)
    
print("----")

for c in "hello world":
    print(c)
print("----")
for d in {'1':"MAD",'2':"YU"}:
    print(d)
print("----")

# http://anandology.com/python-practice-book/iterators.html


'''ITERATION PROTOCOL
       The built-in function iter takes an iterable object and returns an iterator.
 
 x = iter([1, 2, 3])
 Iterator = iter(iterable_object)
 
>>> x                 O/P  <listiterator object at 0x1004ca850>
>>>x.next()           O/P  1
No elements then "StopIteration"

x = [1, 2, 3]    --- x is an Iterable
>>> y = iter(x)  --- y and z are two individual instances of an iterator, 
>>> z = iter(x)      producing values from the iterable x.


 '''
       
print("********Employee class***************")      
class Employee:

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
        print("DEF CONSTRUCTOR EXEC")
    def __iter__(self):
        print("iter() EXECUTED")
    def __next__(self):
        print("next() EXECUTED")

madhu = Employee(10,"MadhuN",15000)   #madhu is an iterable object
#madhu.__init__()
madhu.__iter__()    # iter(madhu)  gives Iterator object
madhu.__next__()    # next(madhu)  gives each elements during iteration

print("********Employee class***************")

 ####  http://nvie.com/posts/iterators-vs-generators/
class yrange:
    
    def  __init__(self,n):
        self.i=0
        self.n=n
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.i<self.n:
            i=self.i
            self.i+=1
            return i
        else:
            print("---Iteration completed----")
            try:
                raise StopIteration()
            except StopIteration as si:
                print(si)
                print("Iteraation got completed.There are no further values to iterate :: ",si)
        
print("-----yrange iterator------------")
        
y = yrange(3)   # y is an iterable object, y.iter() ====> iterator object
print(y.next()) 
print(y.next())
print(y.next()) 
print(y.next())  
#list(yrange(5))   #[0,1,2,3,4] 
   
print("-----range iteraotr-----------")
for i in range(3):
    print(i)

 


      