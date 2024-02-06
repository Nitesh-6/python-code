# REQUIREMENT: Find sum of 2 positive** numbers and give the result

# 1st approach : No one writes validation logic
print("1st approach : Without validation----------")

# State
n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))

# Behavior
def sum(num1, num2):
    res = num1 + num2
    return res

print("Addition result :", sum(n1, n2))  # Customer REQ Impl Not Satisfied

# 2nd approach : Write validation logic before function call
print("2nd approach : Validation Before Function call ----------")

def sum(num1, num2):
    res = num1 + num2
    return res

n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))
# validation logic  ********** Code Duplication **********
if n1 >= 0 and n2 >= 0:
    print("Addition result :", sum(n1, n2))
else:
    print("Please enter valid positive number")

# OR
if n1 < 0 or n2 < 0:
    print("Please enter valid positive number")
else:
    print("Addition result :", sum(n1, n2))
print("------------------------")


# 3rd approach : Write validation logic inside function
print("3rd approach : Validation Inside Function ----------")


def sum(num1, num2):
    # validation logic  ********* Code Pollution *************
    if num1 < 0 or num2 < 0:
        return "Please enter valid positive number"
    res = num1 + num2
    return res

n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))

print("Addition result :", sum(n1, n2))

print("------------------------")



print("------------------------")

'''
Below code is also not acceptable 

def _validate_data(n1,n2):
    if n1 < 0 or n2 < 0:
        return False
    else:
        return True

def sum(num1, num2):
    is_valid = _validate_data(num1,num2)
    if is_valid:
        res = num1 + num2
        return res
    else:
        return  "Please enter valid positive number"

'''

'''
Fund Transfer : 
-------------------
    - Check min. balance : pre-activity pre-op 
    - Do funds transfer 
    - Debit, Credit      : post-activity post-op
    
'''



def validate_data(func):
    def wrapper(*args, **kwargs):
        if args[0] >= 0 and args[1] >= 0:
            print("Before method call")
            output = func(*args, **kwargs)
            print("After method call")
            return output
        else:
            return "ERROR DATA"
    return wrapper    # wrapper(10,20)


@validate_data
def sum(n1, n2):
    print("Inside sum method")
    res = n1 + n2
    return res

print("Addition : ", sum(10, 20))   # sum (10,20)



# Division result


def validate_den(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            return "Invalid denominator"
        else:
            output = func(*args, **kwargs)
            return output
    return wrapper
n1 = 10
n2 = 3

@validate_den
def divide(num1, num2):
    res = num1 / num2
    return res

print("Division result : ", divide(n1, n2)) # divide (n1, n2)






