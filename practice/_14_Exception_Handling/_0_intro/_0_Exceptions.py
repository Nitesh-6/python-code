# https://docs.python.org/3/library/exceptions.html
''''''
'''
Exception: Can be handled : try, except  blocks
Error    : Cant be handled : 
                  : Memory Errors 
                  : System exits


BaseException
 +-- Exception***          (Polygon)
      +-- ArithmeticError *       Quadrilateral
      |    +-- FloatingPointError       Square
      |    +-- OverflowError
      |    +-- ZeroDivisionError *
      +-- AssertionError *
      +-- ImportError
      |    +-- ModuleNotFoundError *
      +-- LookupError
      |    +-- IndexError *
      |    +-- KeyError *
      +-- NameError *
      |    +-- UnboundLocalError
      +-- OSError *
      +-- RuntimeError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError *
      +-- ValueError *
           '''
print("Type error example")
print("Additions: ", 10 + 'Madhu')   # TypeError Exception
print("ZDE example")
print("Division : ", 10/0)  # ZeroDivisionError exception

'''
Exception Details 
    - Header
    - File complete path, line# 
    - Statement  
    - Type of Exception and its message
    
employee records: 10 records : 100 records 
li = []
# Third highest salary 
    sort list in descending order of salary 
    - li[2] 
    
- Rare scenario: 0 records from database 


ZeroDivisionError: 
----------------------
# Calculating aggregate 
    num/den : x+y/x2-2y

ATM Center: pin#, amount, withdraw: 
    - Amount debit from your account 
    - Withdrawl 
    

'''
