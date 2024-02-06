


class ExamResult:
    def __init__(self):
        pass

    def get_st_result(self, marks):
        if marks >= 0 and marks <= 100:
            # return "Valid Marks"
            if marks >= 35:
                # return "PASS"
                if marks >= 60:
                    return "First Class"
                elif marks >= 50:
                    return "Second Class"
                else:
                    return "Third Class"
            else:
                # return "FAIL"
                pass
        else:
            # return "Invalid Marks"
            pass
sai = ExamResult()
print(sai.get_st_result(65))