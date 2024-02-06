from unittest import TestCase
from student_result import ExamResult


class TestExamResult(TestCase):
    def setUp(self) -> None:
        self.obj = ExamResult()
    '''
    def test_get_st_result_valid(self):
        marks = 45
        exp_res = "Valid Marks"
        act_res = self.obj.get_st_result(marks)
        self.assertEqual(exp_res, act_res, "Both should be same")

    def test_get_st_result_invalid(self):
        marks = 200
        exp_res = "Invalid Marks"
        act_res = self.obj.get_st_result(marks)
        self.assertEqual(exp_res, act_res, "Both should be same")
    
    def test_get_st_result_pass(self):
        marks = 45
        exp_res = "PASS"
        act_res = self.obj.get_st_result(marks)
        self.assertEqual(exp_res, act_res, "Both should be same")

    def test_get_st_result_fail(self):
        marks = 20
        exp_res = "FAIL"
        act_res = self.obj.get_st_result(marks)
        self.assertEqual(exp_res, act_res, "Both should be same")
    '''
    def test_get_st_result_first(self):
        marks = 80
        exp_res = "First Class"
        act_res = self.obj.get_st_result(marks)
        self.assertEqual(exp_res, act_res, "Both should be same")

    def test_get_st_result_second(self):
        marks = 55
        exp_res = "Second Class"
        act_res = self.obj.get_st_result(marks)
        self.assertEqual(exp_res, act_res, "Both should be same")

    def test_get_st_result_third(self):
        marks = 40
        exp_res = "Third Class"
        act_res = self.obj.get_st_result(marks)
        self.assertEqual(exp_res, act_res, "Both should be same")
