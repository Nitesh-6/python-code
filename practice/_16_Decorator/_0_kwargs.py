# **KWARGS : Keyword Arguments: dictionary format


print("================ KWARGS Keyword Arguments==================")
print("---------Program 1 --------------")

def myFun(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print("VALUE : %s == %s" % (key, value))

myFun()   # {} Empty Dictionary
myFun(10, 20, 30)
myFun(first='Madhu', mid='Sudhan', last='Nettem')  # dictionary
             # {first='Madhu', mid='Sudhan', last='Nettem'}
print("---------Program 2 --------------")

def myFun(val, **kwargs):
    print("First parameter : ", val)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    print("************")

# myFun() # Error
myFun(10)
myFun("Hi", first='Geeks', mid='for', last='Geeks')
myFun(val="Hi", first='Geeks', mid='for', last='Geeks')
# myFun(x="Hi", first='Geeks', mid='for', last='Geeks') # ERROR

print("----Program 3---------")
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

myFun("Geeks", "for", "Geeks")

args = ("Geeks", "for", "Geeks")
myFun(*args)  #myFun("Geeks", "for", "Geeks") Tuple Packing, unpacking

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
