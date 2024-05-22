from dbmanager import DatabaseManager
import authentication
from tkinter import messagebox



class Appointment:
    global database_manager

    def __init__(self):
        self.database_manager = DatabaseManager()

    def addAppointment(self, facultyID:str, selectedDate:str, selectedTime:str,studentID:str):
        auth = authentication.authentication()
        foundFaculty = 0
        try:
            self.database_manager.connectDatabase()
            try:
                auth.findEmployee(facultyID)
                addappointmentQuery = "INSERT INTO appointment VALUES ('{}','{}','{}','{}')".format(facultyID,
                                                                                                    selectedDate,
                                                                                                    selectedTime,
                                                                                                    studentID)
                self.database_manager.execute(addappointmentQuery)
            except Exception as ex:
                raise ex
        except Exception as e:
            raise e
        if not facultyID == "" or not selectedTime == "" or not foundFaculty == -1:
            self.database_manager.coomitChanges()


    def viewAppointmentData(self,student_id: str):
        getappointmentQuery = "SELECT *FROM appointment WHERE student_id='{}'".format(student_id)

        self.database_manager.connectDatabase()
        try:
            result = self.database_manager.execute(getappointmentQuery)
            if len(result) == 0:
                messagebox.showerror("NO DATA", "NO DATA")
            return result
        except:
            print('value nai')

        self.database_manager.connection_close()

    def viewTeacherAppointment(self,employeeID:str):
        getTeacherAppointmentQuery = "SELECT *FROM appointment WHERE employee_id='{}'".format(employeeID)

        self.database_manager.connectDatabase()
        try:
            result = self.database_manager.execute(getTeacherAppointmentQuery)
            if len(result) == 0:
                messagebox.showerror("NO DATA","NO DATA")
            else:
                print(result)
                return result
        except:
            print('value nai')
        self.database_manager.connection_close()

