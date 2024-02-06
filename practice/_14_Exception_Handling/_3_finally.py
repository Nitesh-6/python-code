'''
Reading book : Completed  : Close it
             : Incomplete : Close it

'''
try:
    print("In try block: Open Operations")
    print("---Opening any File----")
    print("---Opening DB Connection---")
except:
    print("In except block")
else:
    print("In else block")
finally:
    print("In finally block: Closing Operations")


print("*******************************************************")
try:
    print("In try block")
    raise Exception("Sample Exception")
except:
    print("In except block")
else:
    print("In else block")
finally:
    print("In finally block")