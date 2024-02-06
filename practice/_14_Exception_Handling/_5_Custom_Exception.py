'''
@author: madhu
'''

class AgeError(Exception):   # AgeError is a  Exception (Custom/Userdefined)
    """Exceptions raised for errors in input
       Attributes:
         Expression : Input expression in which error occured.
         Message    : Explanation of error
    """
    '''
    def __init__(self,expression,message):
        self.expression=expression
        self.message=message
    ''' 
    def __init__(self, message):
        self.message = message
'''
try:
    age = int(input("Enter your age"))
    if(age >= 18): #Raise exception
        print("---You are eligible to vote-------")
    else:
        raise Exception("Not eligible") # manually raising exception as per our use case
    print("-----Voting process completed------")
except Exception as ageex:   # Exception ageex = Exception("Not eligible")    # 5L Can <== 5L Water
    print(ageex)



try:
    age = int(input("Enter your age"))
    if(age >= 18): #Raise exception
        print("---You are eligible to vote-------")
    else:
        raise AgeError("Not eligible") # manually raising exception as per our use case
    print("-----Voting process completed------")
except AgeError as ageex:   # AgeError ageex = AgeError("Not eligible")    # 2L Can <== 2L Water
    print(ageex)

'''

try:
    age = int(input("Enter your age :"))
    if age < 18:
        raise AgeError("**Not eligible**")  # manually raising exception as per our use case
    print("---You are eligible to vote-------")
    print("-----Voting process completed------")
except Exception as ageex:  # Exception ageex = AgeError("Not eligible")    # 5L Can <== 2L Water  float x = 10
    print("Exception :", ageex)
except AgeError as aer:  # NO USE
    print("AgeError :", aer)

'''
Correct approach
----------------
except AgeError as aer:
    print("AgeError :", aer)
except Exception as ageex: 
    print("Exception :", ageex)


 +-- Exception***          (Polygon)
      +-- ArithmeticError *       Quadrilateral
      |    +-- FloatingPointError       Square
      |    +-- OverflowError
      |    +-- ZeroDivisionError *
      
      
# # 10: ArithmeticError
# # 15: ZeroDivisionError 

 
except ZeroDivisionError as zde: 
except ArithmeticError as a:
except Exception as e: 

'''


