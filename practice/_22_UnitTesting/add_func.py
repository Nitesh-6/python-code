# Get addition and addition of squares of 2 numbers
from pack.b import Employee


class Addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        obj = Employee(10, 'Madhu')
        output = obj.get_edata()
        f_out = result + output
        return f_out

    def get_squares(self):
        result = self.num1 ** 2 + self.num2 ** 2
        return result


'''
# Manual Test Script
# STATE
    # 1. Prepare input data
        n1 = 10
        n2 = 20
    # 2. Create object
        obj = Addition(n1, n2)
# Behavior 
  # 3. Expect the output
        Our Assumption         ==>  Addition result : 30
  # 4. Method Call and get result 
        act_res = obj.add()
# 5. Actual Output : 
        Print returned result  ==> Addition result : 30
# 6. Compare the results(actual op with our expected op)
        If both are same : Code is working fine 
                not same |: Issue with code 

'''
'''
Expected output : 30  ==> Assumption 
Actual   output : 30  ==> App response
'''

# Student result : Validation, Pass/Fail,  1st/2nd/3rd
'''
1. Give wrong input: <0 >100
2. Pass Fail       : >=35 <35 
3. 1st,2nd,rd      : 35-50 50-60 >60
'''
