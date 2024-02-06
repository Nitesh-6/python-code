'''
@author: madhu
'''


def get_number(x, y):
    try:
        print("-----IN TRY BLOCK--------")
        result = x / y
        print("The result for division is : ", result)
        # float_res = round(24.601 / 0.01234, 4.6)
    except Exception as err:  # Exception err = ZeroDivisionError()
        print("---EXCEPTION: Occured -----", err)
    else:
        print("--------In ELSE block---------")


print("----Before function call -----")
get_number(20, 0)
print("----After function call -----")
