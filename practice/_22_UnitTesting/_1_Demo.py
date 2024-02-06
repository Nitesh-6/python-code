''''''

# Student result
'''
1. Validation 
2. Result 
3. Division 
4. Distinction 
5. Cent marks 
'''
# State
marks = -10
# Behavior
if marks >= 0 and marks <= 100:
    print("Valid Marks")
    if marks >= 35:
        pass
    else:
        pass
else:
    print("Invalid Marks")

'''
# TDD:
---------
Code it 
Test it (unit test cases) : Fails 
fix the test case 
Retest : success:
Write new Code
Retest : fails 
Fix the test case : 
Write Code 

After enhancements : 1 : Function level 
                      5 : Function usage scenarios 
       Controller           Service         DAO 
        f1()                f2()            f3()                helper()    
            f2()               f3()             helper()              utilities()

Avoid in detail Manual Testing           
        - Write unit test cases* : unittest       
'''
# Find even or odd number
num = 5
if num % 2 == 0:
    print("Even number : ", num)
else:
    print("Odd number : ", num)

'''
Internal 
Working Code 
Test : Expected Result : Our assumption
       Actual Result   : Console 
'''

'''
Unit Testing:
----------------
- Assuming external environment is working fine, 
  we should check how our unit is responding.
- If any external dependencies are there for our unit 
        - use mock frameworks to provide stub values 
            - mock 
            - pytest * 
            - magicmock 
            
  
'''
