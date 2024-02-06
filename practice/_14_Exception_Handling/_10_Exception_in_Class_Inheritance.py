'''
@author: madhu
'''

class A(Exception):
    pass
class B(A):
    pass
class C(B):
    pass

for cls in [A, B, C]:
    try:
        raise cls()  # raise A() raise B() raise C()
    except C:           #  C c = A() invalid
        print("C")
    except B:           # B b = A() invalid
        print("B")
    except A:           # A a = A() valid
        print("A")
        
print("----------")

class X(Exception):
    pass
class Y(X):
    pass
class Z(Y):
    pass

for cls in [X,Y,Z]:
    try:
        raise cls()
    except Z:         # ZeroDivisionError
        print("Z")
    except Y:         # ArithmeticError
        print("Y")
    except X:
        print("X")    # Exception
    
    
    '''
    except X:         # Exception
        print("X")
    except Y:         # ArithmeticError
        print("Y")
    except Z:
        print("Z")    # ZeroDivisionError
    '''

def m1(r1, r2):
    print("---m1 method--")
    return r1/r2
    '''
    try:
        result = r1/r2
        return result
    except Exception as e:
        print("Exception occured: ", e)
    return "Invalid input data"
    '''
def m2(p1, p2):
    print("---m2 method--")
    r = m1(p1, p2)
    return r

def m3(a, b):
    print("---m3 method--")
    m = m2(a, b)
    return m

def m4(n1, n2):
    print("---m4 method--")
    n = m3(n1, n2)
    return n

print("Divsion result  ", m4(10, 0))

'''
- Code review 
- Code Refactoring (based on peer comments) 
'''