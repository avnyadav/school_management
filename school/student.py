
class Student:
    

    def __init__(self,std_fname,std_Mname,std_lname,student_age,student_address,student_standard,student_grade):
        self.std_fname:str = std_fname
        self.std_Mname:str = std_Mname
        self.std_lname:str = std_lname
        self.student_age:int = student_age
        self.student_address:str = student_address
        self.student_standard:str = student_standard
        self.student_grade:str = student_grade

    @staticmethod
    def get_grade():
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
