
class Student:
    total_marks = 600
    sub = Subject()

    def __init__(self,student_name,student_age,student_address,student_grade)
        self.student_name:str = student_name
        self.student_age:int = student_age
        self.student_address:str = student_address
        self.student_standard:str = student_standard
        self.student_grade:str = student_grade

    @classmethod
    def get_grade(cls,percentage):
        if percentage > 80:
            return "O"
        
        elif percentage > 60:
            return "A"

        elif percentage > 50:
            return "B"
        
        elif percentage > 35:
            return "C"
        else:
            return "Fail"
    
    @classmethod
    def get_percentage(cls,marks):
        return (marks*100)/cls.total_marks
