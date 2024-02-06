s = 10
x = 2

try:
    res = s / x
    print(res)
except ZeroDivisionError as zde:
    print("Zero division error:", zde)
except TypeError as te:
    print("Type error:", te)
except Exception as e:
    print("Exception occurred:", e)
else:
    print("there is no exception")
finally:
    print("it executed")
