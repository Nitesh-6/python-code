
# 2. NESTED FUNCTIONS :
print("---------------2. NESTED FUNCTIONS------------------")

def parent():
    print("Before Nested Function")
    def child():  # nested function
        return "In nested func : first_child()"
    print("After Nested Function")
    print("Inside parent :", child)
    print("Inside parent :", child())
    return child  # <function parent.<locals>.child at 0x000001B0034A3BF8>

# fchild = parent.child()  ERROR
f_child = parent()
print("Outside parent :", f_child())  # child()
print("Outside parent :", f_child)


# parent.first_child()  # It gives error
# parent.first_child()  This is not the way to call nested function

print("Parent function address: ", parent)  # parent = <function parent1 at 0x000001BF373B1E18>   x = 10

print("---Parent function call :-----")
print(parent())
nest_func_addr = parent()

print("Calling  nested function from outside function      : ", nest_func_addr())  # 12 line
print("Printing nested function name from outside function : ", nest_func_addr)    # 13 line

print("------Using EXCEPTION HANDLING ---------------- ")
try:
    #parent.first_child()
    f_child = parent()
    print("Calling child function : ", f_child())
except AttributeError as err:
    print("Exception :: ", err)
    print("--You cannot call nested function directly------")

print("---------------------------------------------------")