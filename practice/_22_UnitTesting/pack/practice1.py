class Student:
    def __init__(self):
        pass

    def get_result(self, marks):
        if marks <= 100 or marks >= 0:
            if marks >= 35:
                if marks >= 75:
                    print(f"The result is Distension")
                elif marks >= 65:
                    print(f"The result of is First class")
                elif marks >= 55:
                    print(f"The result of is Second class")
                elif marks >= 45:
                    print(f"The result of is Third class")
                else:
                    print(f"The result of is just pass")
            else:
                print("your result is fail")
        else:
            print("Invalid marks")


nitesh = Student()
nitesh.get_result(90)
