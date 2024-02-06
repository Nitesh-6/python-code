from b import find_data, Employee


def get_data():
    print("Controller ")
    x = 10
    y = 20
    res = find_data(x, y)


def get_info():
    obj = Employee(10, 'Madhu N')
    res = obj.get_edata()
    output = res ** 4
    return output
