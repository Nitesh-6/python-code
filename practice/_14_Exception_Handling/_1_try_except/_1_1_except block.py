# After Exception handling
print("---- I. Exception Handling----")
try:
    x = int(input("Enter numerator2 value :"))
    y = int(input("Enter denominator2 value :"))
    result = x / y  # ZeroDivisionError("division by zero")  object  : Employee(10,'Madhu',15000)
    print("Division :", result)  #  any value/0 = infinity
    print("---Division result usage---")
    print("---In try block3 ---")
except:
    print("EXCEPTION1 :: SOME Exception Occured")
print("---Remaining code II---")
print("---------------------------------")