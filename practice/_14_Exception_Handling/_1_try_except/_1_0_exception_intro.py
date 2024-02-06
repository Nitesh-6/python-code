'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/Batch_13/B13_PythonTraining/_13_Exception_handling/_1_Introduction.py", line 20, in <module>
    x = int(input("Enter numerator value :"))
ValueError: invalid literal for int() with base 10: 'dfgads'
'''

'''
Requirement: As an end user i will give 2 values,
             display division result for the same.
   
   If failure:  User entered numbers not valid   --- Display failure message
   If success:  User entered numbers             --- Display result
                 - If abnormal situation(denominator is 0) 
                             ---------------Display the exception message           
'''
# Before Exception handling
print("----Before Exception handling----")

x = int(input("Enter numerator value :"))    # ValueError
y = int(input("Enter denominator value :"))  # ValueError
result = x/y  # ZeroDivisionError("division by zero") # value/0 = Infinity
print("Division :", result)

print("Remaining Code")
print("---------------------------------")

'''
Blocks   : if elif else for while  function class

Blocks to handle the exception
===============================    
try*      : Code which causes the exception
except*   : To catch/handle exception occured in try block
else      : 
finally   :
'''


'''
4 ways to handle Exception:
===============================
1. except:                          -->  It will handle any exception from try block 

2. except Exception as e:           --->  It will handle any exception from try block

3. except ZeroDivisionError as zde: ---> Write specific exception class name

4. except ValueError as v:
   except ZeroDivisionError as zde
   except Exception as e:           ---> Perfect/Ideal approach
   
   
- To handle only one Exception : 1 2 3 
- To handle mulitple exceptions: 1 2 4
'''

# After Exception handling
print("---- Type I. Exception Handling----")
try:
    x = int(input("Enter numerator2 value :"))
    y = int(input("Enter denominator2 value :"))
    result = x / y  # ZeroDivisionError("division by zero")  object  any value/0 = infinity
    print("Division :", result)
except:
    print("EXCEPTION1 :: SOME Exception Occured")
print("---Remaining code II---")
print("---------------------------------")
'''
Specification: As a sub class, 
        - Reuse super class methods through inheritance 
        - Override them in sub class 
        - Dont create your own methods in sub class 
        
Employee emp = SoftwareEmp()      5L Can <--- 2L Water
Animal a = Tiger() 
Animal a = Lion() 
Animal a = Cat() 
Animal a = Dog()
5L : 1L 2L 3L 4L 5L
Inheritance :
----------------
Employee   5L Can
SoftwareEmployee 2L Can

I.  Employee madhu  = Employee(100,'Madhu',2000)
II. SEmployee madhu = SEmployee(100,'Madhu',2000)
III.Employee madhu  = SEmployee(100,'Madhu',2000)  # Upcasting  90%
IV. SEmployee madhu = Employee(100,'Madhu',2000)  # Downcasting X

'''


print("---- Type II. Exception Handling----")
try:
    x = int(input("Enter numerator3 value :"))  # ValueError("invalid.....")
    y = int(input("Enter denominator3 value :"))
    result = x / y  # ZeroDivisionError("division by zero")
    print("Division :", result)  #  any value/0 = infinity
    print("---Division result usage---")
    print("---In try block3 ---")
except Exception as exec:
    print("EXCEPTION2 OCCURED  :: ", exec)
              # III. Exception exec = ValueError("invalid.....")   5L Can <== 0.5L 1L 2L 3L 4L 5L
                  # Exception exec = ZeroDivisionError("division by zero")
                                # Employee emp  = SoftwareEmployee()
                                # float x = 10
                                # 5L : 2L
                                # Animal a = Tiger()


print("---Remaining code II---")
print("---------------------------------")


print("---- Type III. Exception Handling----")
try:
    print("Hello World")
    x = int(input("Enter numerator2 value :"))    # ValueError("invalid.....")
    y = int(input("Enter denominator2 value :"))  # ValueError("invalid.....")
    result = x / y  # ZeroDivisionError("division by zero")
    print("Division :", result)
    li = [1, 2, 3, 4]
    print("List value : ", li[2])       # IndexError
    # print("Data : ", 10 + "Python")
    print("---Division result usage---")
    print("---In try block3 ---")
except ValueError as v:  # II. ValueError v = ValueError("invalid.....")  # int x = 10
        # ValueError v = ZeroDivisionError("division by zero")  # INVALID
    print("ValueError :: ", v)
except ZeroDivisionError as zde:  # ZeroDivisionError zde = ZeroDivisionError("division by zero")
    print("ZeroDivisionError :: ", zde)
except IndexError as ie:  # IndexError ie = IndexError("division by zero")
    print("ZeroDivisionError :: ", ie)

print("---Remaining code III---")
print("---------------------------------")
# int x = 10

# After Exception handling
print("---- IV. Exception Handling----")
try:
    x = int(input("Enter numerator4 value :"))   # ValueError
    y = int(input("Enter denominator4 value :"))
    result = x / y                               # ZeroDivisionError
    li = [1, 2, 3]  # UI or Database
    print("List index val : ", li[2])   # IndexError( forgot to write as except block)
    print("Division :", result)
    print("Data : ", 10 + "Python")  # TypeError("MSG")
    print("---Division result usage---")
    print("---In try block4 ---")
except ValueError as ve:  # ValueError ve = ValueError("msg")
    print("ValueError occured4 : ", ve)
except ZeroDivisionError as zde:  # ZeroDivisionError e = ZeroDivisionError("ERROR MSG")
    print("ZeroDivisionError occured4 : ", zde)
except IndexError as ie:
    print("Index Error : ",  ie)
except Exception as e:     # Exception e = TypeError()
    print("EXCEPTION occured : ", e)
print("---Remaining code IV---")
print("---------------------------------")

