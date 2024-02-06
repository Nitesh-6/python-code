# unit _0_str_len_1 cases
from unittest import TestCase
from add_func import Addition

class TestAddition(TestCase):

    def setUp(self):
        n1 = 10   # 1
        n2 = 20
        self.obj = Addition(n1, n2)  # 2

    def test_add(self):
        exp_res = 40  # 3
        act_res = self.obj.add()  # 4  ( 5 don't do it)
        self.assertEqual(exp_res, act_res, "*****Both should be equal*****")  # 5

    def test_get_squares(self):
        exp_res = 500
        act_res = self.obj.get_squares()
        self.assertEqual(exp_res, act_res, "*****Both should be equal*****")

'''
During Execution
1. Loads and create object of TestAddition  ta = TestAddition()
2. Calls setUp method : ta.Setup()
3. Calls _0_str_len_1 method  : ta.test_add()
'''

