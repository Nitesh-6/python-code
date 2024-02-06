
# Get division result of 2 numbers

def validate_div(func):
    def wrapper(*args, **kwargs):   # (10, 0)
        if args[1] != 0:
            output = func(*args, **kwargs)
            return output
        else:
            return "Invalid denominator"
    return wrapper

@validate_div
def divide(n1, n2):
    result = n1/n2
    return result

print("Division  result : ", divide(10, 0))

print("-------------------------------------------------")
def validate_div(func):
    print("-----Decorator: validate function-------")
    def wrapper(*args, **kwargs):   # (10, 0)
        print("-----Nested func: wrapper function-------")
        if args[1] != 0:
            print("----Pre: Before function call-----")
            output = func(*args, **kwargs)
            print("----Post: After function call-----")
            return output
        else:
            return "Invalid denominator"
    return wrapper

@validate_div
def divide(n1, n2):
    print("-----divide function-------")
    result = n1/n2
    return result

print("Division  result : ", divide(10, 2))


print("====================FUND TRANSFER====================")


def validate_bal(func):
    def wrapper(*args, **kwargs):
        if args[0] <= 5000:
            print("Verified Balance")
            out = func(*args, **kwargs)
            print("Send SMS, Email message")
            return out
        else:
            return "Insufficient funds"
    return wrapper

@validate_bal
def fund_transfer(amount):
    print("Fund Transfer Successful : ", amount)
    return "SUCCESS"

print("Transfer the funds : ", fund_transfer(1000))




def validate_den(func):
    def wrapper(*args, **kwargs):
        if args[1] != 0:
            output = func(*args, **kwargs)
            return output
        else:
            return "Invalid Denominator"
    return wrapper



@validate_den
def divide(n1, n2):
    res = n1 / n2
    return res

print("Division result : ", divide(10, 0))

