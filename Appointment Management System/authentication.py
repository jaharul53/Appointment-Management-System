from tkinter import messagebox
from dbmanager import DatabaseManager


class authentication:
    global database_manager

    def __init__(self):
        self.database_manager = DatabaseManager()

    def findEmployee(self, employee_id: str):
        teacher_query = "SELECT *FROM teacher WHERE employee_id='{}' ".format(employee_id)
        self.database_manager.connectDatabase()
        try:
            result = self.database_manager.execute(teacher_query)
            teacer_id = result[0]
            return (teacer_id)
        except Exception as e:
            messagebox.showerror("invalid input", "INVALID INPUT")
            raise e

    def authenticate_employee(self, employee_id: str, department: str):
        teacher_query = "SELECT *FROM teacher WHERE employee_id='{}' AND department='{}'".format(employee_id,
                                                                                                 department.upper())
        self.database_manager.connectDatabase()
        try:
            result = self.database_manager.execute(teacher_query)
            teacer_id, dept = result[0]
            return (teacer_id, dept)
        except Exception as e:
            raise e

    def authenticate_student(self, student_id: str, section: str, department: str):
        student_query = "SELECT *FROM student WHERE student_id='{}' AND section='{}' AND department='{}'".format(
            student_id, section.upper(), department.upper())
        try:
            self.database_manager.connectDatabase()
            result = self.database_manager.execute(student_query)
            student_roll, sec, dept = result[0]
            return (student_roll, sec, dept)
        except Exception as e:
            raise e
