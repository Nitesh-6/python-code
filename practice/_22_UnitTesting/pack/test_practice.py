from unittest import TestCase
from practice1 import Student


class Student_test(TestCase):
    def setUp(self) -> None:
        self.obj = Student()

    def get_stu_res_dist(self):
        marks = 90
        exp_res = "The result is Distension"
        act_res = self.obj.get_result(marks)
        self.assertEqual(exp_res, act_res, "both the values should be equal")

    def get_stu_res_first(self):
        marks = 67
        exp_res = "The result of is First class"
        act_res = self.obj.get_result(marks)
        self.assertEqual(exp_res, act_res, "both the values should be equal")

    def get_stu_res_second(self):
        marks = 57
        exp_res = "The result of is Second class"
        act_res = self.obj.get_result(marks)
        self.assertEqual(exp_res, act_res, "both the values should be equal")

    def get_stu_res_third(self):
        marks = 50
        exp_res = "The result of is Third class"
        act_res = self.obj.get_result(marks)
        self.assertEqual(exp_res, act_res, "both the values should be equal")
