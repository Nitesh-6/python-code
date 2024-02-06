'''

'''
li = []
for x in range(10):
    li.append(x)
print(li)

# List comprehension

li = [x for x in range(10)]
print(li)

print([x for x in range(10)])


li = []
for x in range(10):
    li.append(x ** 2)
print(li)

li = [x ** 2 for x in range(10)]
print(li)




# List comprehension
li = [x ** 2 for x in range(10)]
print(li)

li = []
for x in range(10):
    li.append(x**2)
print(li)


li = [x for x in range(10)]   # x = 10 print(x)
print(li)


li = []
for x in range(10):
    li.append(x ** x)
print(li)

print([x ** x for x in range(10)])




#     syntax: [expression for var in sequnce]
print([x**x for x in range(10)])


li_eq = [x*x for x in range(10)]
print(li_eq)


'''
 http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

List comprehensions are a tool for transforming one list (any iterable actually) into another list.
 During this transformation, elements can be conditionally included in the new list and each element
  can be transformed as needed.
'''

print([x+10 for x in range(1, 10)])

li = []
for x in range(1, 10):
    li.append(x+10)
print(li)