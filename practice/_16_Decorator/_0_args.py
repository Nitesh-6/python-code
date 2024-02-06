# https://www.geeksforgeeks.org/args-kwargs-python/
# *args  : tuple format     : any number of arguments
'''
@staticmethod
@classmethod
@abstractmethod
@property
        *000  %123
'''

print("----Program 1 -------------")

def my_fun(*args):   # function overloading
    print(args, "----", type(args))
    for val in args:
        print(val)
    print("*******")

my_fun()  # my_fun ()
my_fun("Python")  # ("Python",)
my_fun('Hello', 'Welcome', 'to', 'Geeks for Geeks')
my_fun(1, 2, 3, 4, 5)
my_fun(1, 2.4, 'Madhu', True, [1, 2, 3], (1, 2, 3), {1:1, 2:2}, {11, 2, 3})



print("-------Program 2----------------")
def my_func(val, *args):
    print("First argument :", val, "------", args)
    for arg in args:
        print("Next argument through *argv :", arg)

# myFun()    # ERROR
my_func(100)   # val = 100   args = ()
my_func(100, 'Madhu Nettem')  # val = 100   args = ("Madhu Nettem",)
my_func('', 'Welcome', 'to', 'GeeksforGeeks')

