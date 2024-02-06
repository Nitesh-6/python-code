'''
@classmethod
@staticmethod
@abstractmethod
@property
'''



# Let Decorator take care of Validation
print("----------With Decorator----------")
'''
  1 *args **kwargs
  2 first class function
  3 nested(wrapper) function
  4 returning nested function


def validate_data(func):
    def wrapper(*args, **kwargs):
        if args[0] >= 0 and args[1] >= 0:
            output = func(*args, **kwargs)  # sum(10,20)
            return output
        else:
            return "Invalid Data"
    return wrapper

'''
def validate_data(func):
    def wrapper(*args, **kwargs):
        print("PRE : Before function call")
        output = func(*args, **kwargs)  # sum(10,20)
        print("POST: After function call")
        return output
    return wrapper

def validate_data(func):
    def wrapper(*args, **kwargs):
        if args[0] >= 0 and args[1] >= 0:
            output = func(*args, **kwargs)
            # post activities
            return output
        else:
            return "Invalid Data"
    return wrapper

@validate_data
def sum(num1, num2):
    print("In sum call")
    res = num1 + num2
    return res

n1 = 10 # int(input("Enter number 1  :"))
n2 = -5  # int(input("Enter number 2  :"))

print("Addition result :", sum(n1, n2))

             # P1: sum  validate_data(sum)
            #  P2: (10,20)  wrapper(10,20)

# Python ==> validate_data(sum)  ==>  wrapper + (10,20) ==> wrapper(10,20)



print("------------------------------------------------------")
'''
Step1 : Our function call will be divided into 2 parts   39th line
        sum(10,20) ==>      sum                (10,20)
                            1. function name   2. arguments 
Step2 : Decorator function will be called by passing our function as argument
                validate_nums(sum)
        Decorator function validate_num(sum) will get executed and 
        it returns nested function(i.e, wrapper) to python interpreter
Step3 : Python will execute wrapper function by combining arguments
        wrapper + (10,20) ==> wrapper(10,20)
        Here inside it will validate the data 
          If success : performs the method call 
          else       : returns exception message    
'''

def validate_val(func):
    def wrapper(*args, **kwargs):
        if args[1] != 0:
            output = func(*args, **kwargs)
            return output
        else:
            return "Invalid Denominator"
    return wrapper


@validate_val
def divide(num1, num2):
    result = num1 / num2
    return result

print("Division result : ", divide(10, 0))

print("==================================================")

'''
Steps:
-------
1. 71 Line will try to call divide method 
2. Found that divide has decorator
3. Function will be divided into 2 parts 1. divide 2. (10,2)
4. Calls decorator function by passing divide(function name) to func
5. Nested wrapper function name will be returned to Python 
6. PI will load wrapper and combines 2nd part wrapper(10,2) to wrapper(*args, **kwargs)
7. wrapper will be executed
8. Inside wrapper we have validation logic args[1] 
9. If the validation is 
        Success: Main function call will happen func(*args, **kwargs)
                 And returns function value to calling place.
        Fail   : Returns error message to calling place.
                 


'''

print("--------FUND TRANSFER FUNC.---------")
'''
1. Check minimum balance
2. Fund transfer
3. Send email, SMS to customer
'''

def validate_cust(func):
    def wrapper(*args, **kwargs):
        print("----1. Check Min. Balance-----")
        func(*args, **kwargs)
        print('---3. Send EMAIL, SMS---------')
    return wrapper

@validate_cust
def fund_transfer():
    print("2.1 Start Fund Transfer")
    print("2.2 Complete Fund Transfer")


print("FUNDS : ", fund_transfer())


def validate_data(func):
    print("Before decorator")
    def wrapper(*args, **kwargs):
        print("Before : Wrapper")
        if args[1] == 0:
            return "Invalid input"
        output = func(*args, **kwargs)  # divide(10,0)
        print("After : Wrapper")
        return output
    print("After decorator")
    return wrapper

print("----------------------------------------")
@validate_data
def divide(n1, n2):
    print("Inside divide method")
    result = n1/n2
    return result


print("Division result  ", divide(10, 20))  # divide    (10, 0)

'''
1. At runtime, I have to decide dynamically whether to call a method or not
2. Before and After calling Method, implement generic functionality
'''






print("----------DIVISON LOGIC---------")

n1 = 10
n2 = 0

def validate_den(func):
    def wrapper(*args, **kwargs):
        if args[1] != 0:
            output = func(*args, **kwargs)
            return output
        else:
            return "Invalid Denominator"
    return wrapper


@validate_den
def divide(num1, num2):
    res = num1 / num2
    return res

print("Division result : ", divide(n1, n2))









