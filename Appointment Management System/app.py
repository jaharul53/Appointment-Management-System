from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkcalendar import DateEntry
from tkinter import messagebox
from authentication import authentication
from appointment import Appointment


class App:
    def __init__(self):
        setUpGui()

def setUpGui():
    #necessary variables:
    global root,favicon,helvitika,firstFrame,diuImg,diuImgLable,teacherBtn,orLabel,studentBtn,studentLoginFrame
    global studentIdInputLable,studentIdInput,sectionInputLable,sectionInput,departmentInputLable,departmentInput_student
    global studentLoginButton,teacherLoginFrame,teacherIdInputLable,teacherIdInput,departmentInputLable,departmentInput
    global teacherLoginButton,teacherBookingsFrame,teacherBookingsFrameLabel,currentBookingBtn,upComingBtn
    global previousBookingBtn,studentBookingFrame,studentBookingsFrameLabel,studentBooingBtn,viewBookingBtn
    global teacherAppointmentFrame,teacherAppointmentFrameLabel,studentBookAppointmentFrame,facultytIdLabel
    global facultytIdInput,appointmentDateLabel,timePickerLable,timePickerInput,submitBtn
    global studentLoginFrameBackBtn, studentId, appointmentDatePicker,studentAppointmentFrame


    #Setting root window:
    root = Tk()
    root.geometry("400x600+450+50")
    root.resizable(False, False)
    root.title('DIU Appointment Management System')
    root.iconbitmap("./assets/diuLogo.png")
    favicon = PhotoImage(file="./assets/diuLogo.png")
    root.iconphoto(False, favicon)

    # used fonts
    helvitika = font.Font(family='Helvetica', size=16)

    # Welcome Screen Code:
    firstFrame = Frame(root, width=400, height=600)
    firstFrame.pack(fill='both',expand=1)

    # Adding DIU logo  in first frame
    diuImg = ImageTk.PhotoImage(Image.open("./assets/diuLogo.png"))
    diuImgLable = Label(firstFrame, image=diuImg)
    diuImgLable.place(x=150, y=50)

    # Adding buttons and text in first frame
    teacherBtn = Button(firstFrame, text="Teacher", padx=8, pady=5, bg='green', fg='#0052cc', font=helvitika,
                        command=showteacherLoginframe)
    teacherBtn.place(x=150, y=250)
    orLabel = Label(firstFrame, text="OR", fg='red', font=helvitika)
    orLabel.place(x=185, y=310)
    studentBtn = Button(firstFrame, text="Student", padx=8, pady=5, bg='#0052cc', fg='green', font=helvitika,
                        command=showstudentLoginFrame)
    studentBtn.place(x=150, y=350)

    #Student Login Frame Code
    studentLoginFrame = Frame(root, width=400, height=600)
    #studentLoginFrame.place(x=0, y=0)

    # Adding input area, lables & button
    studentIdInputLable = Label(studentLoginFrame, text="Your Student id:", fg='black', font=helvitika)
    studentIdInputLable.place(x=50, y=120)

    studentIdInput = Entry(studentLoginFrame,font=helvitika)
    studentIdInput.place(x=50, y=150, width=300, height=30)

    sectionInputLable = Label(studentLoginFrame, text="Section:", font=helvitika)
    sectionInputLable.place(x=50, y=190)

    sectionInput = Entry(studentLoginFrame,font=helvitika)
    sectionInput.place(x=50, y=220, width=300, height=30)

    departmentInputLable = Label(studentLoginFrame,text="Department:",font=helvitika)
    departmentInputLable.place(x=50,y=260)

    departmentInput_student = Entry(studentLoginFrame,font=helvitika)
    departmentInput_student.place(x=50, y=290, width=300, height=30)

    studentLoginButton = Button(studentLoginFrame,text="Login",bg='#0052cc',fg='white',font=helvitika,
                                command=showstudentBookingFrame)
    studentLoginButton.place(x=100,y=400,width=200,height=40)

    studentLoginFrameBackBtn = Button(studentLoginFrame,text="Back",bg='red',fg='white',command=backtowelcome)
    studentLoginFrameBackBtn.place(x=0,y=0)

    #Teacher Login frame code:
    teacherLoginFrame = Frame(root, width=400, height=600)
    #teacherLoginFrame.place(x=0, y=0)

    # Adding input area, lables & button
    teacherIdInputLable = Label(teacherLoginFrame, text="Your Employee id:", fg='black', font=helvitika)
    teacherIdInputLable.place(x=50, y=120)

    teacherIdInput = Entry(teacherLoginFrame, font=helvitika)
    teacherIdInput.place(x=50, y=150, width=300, height=30)

    departmentInputLable = Label(teacherLoginFrame, text="Department:", font=helvitika)
    departmentInputLable.place(x=50, y=190)

    departmentInput = Entry(teacherLoginFrame, font=helvitika)
    departmentInput.place(x=50, y=220, width=300, height=30)

    teacherLoginButton = Button(teacherLoginFrame, text="Login", bg='#0052cc', fg='white', font=helvitika,
                                command=showteacherBookingsFrame)
    teacherLoginButton.place(x=100, y=300, width=200, height=40)

    teacherLoginFrameBackBtn = Button(teacherLoginFrame,text="Back",bg='red',fg='white',command=backtowelcome)
    teacherLoginFrameBackBtn.place(x=0,y=0)

    # Teacher's Bookings frame code:
    teacherBookingsFrame = Frame(root, width=400, height=600)
    #teacherBookingsFrame.place(x=0, y=0)

    # Adding labels & buttons in Teachers Bookings frame :
    teacherBookingsFrameLabel = Label(teacherBookingsFrame,text="Teacher Appointments",fg="#2e86de",font=helvitika)
    teacherBookingsFrameLabel.place(x=95,y=50)

    currentBookingBtn = Button(teacherBookingsFrame,text="Current Bookings",bg="#192a56",fg="#f5f6fa",font=helvitika,
                               command=lambda :getTeacherAppointments(emplyeeId))
    currentBookingBtn.place(x=100, y=150, width=200, height=40)



    teacherBookingsFrameBackBtn = Button(teacherBookingsFrame,text="Back",bg='red',fg='white',command=backtoteacherlogin)
    teacherBookingsFrameBackBtn.place(x=0,y=0)

    #Adding Students Booking Frame code:
    studentBookingFrame = Frame(root, width=400, height=600)
    #studentBookingFrame.place(x=0, y=0)

    #Adding Labels & buttons in Students Booking Frame :
    studentBookingsFrameLabel = Label(studentBookingFrame,text="Students Appointment Booking",fg='#2ecc71',font=helvitika)
    studentBookingsFrameLabel.place(x=60,y=50)

    # Adding labels & buttons in Teachers Bookings frame :
    studentBooingBtn = Button(studentBookingFrame, text="Book An Appointment", bg='#2ecc71', fg='#f5f6fa',
                              font=helvitika,command=showstudentBookAppointmentFrame)
    studentBooingBtn.place(x=90, y=150, width=220, height=40)

    viewBookingBtn = Button(studentBookingFrame,text="View your bookings",bg="#e74c3c",fg="#f5f6fa",font=helvitika,
                            command=lambda :getAppountment(studentId))
    viewBookingBtn.place(x=90, y=220, width=220, height=40)

    studentBookingFrameBackBtn = Button(studentBookingFrame,text="Back",bg='red',fg='white',command=backtostudentlogin)
    studentBookingFrameBackBtn.place(x=0,y=0)

    #Teacher Appontments Frame code:
    teacherAppointmentFrame = Frame(root, width=400, height=600)


    teacherAppointmentFrameLabel = Label(teacherAppointmentFrame,text="Your Appointments",fg="#e74c3c",font=helvitika)
    teacherAppointmentFrameLabel.place(x=110,y=50)

    tracherIdColumnLabel = Label(teacherAppointmentFrame,text="Your ID",font='helvitika 8 bold')
    tracherIdColumnLabel.place(x=50,y=180)

    teacherDateColumnLabel = Label(teacherAppointmentFrame,text="Date",font='helvitika 8 bold')
    teacherDateColumnLabel.place(x=130,y=180)

    teachertimeColumnLabel = Label(teacherAppointmentFrame,text="Time",font='helvitika 8 bold')
    teachertimeColumnLabel.place(x=210,y=180)

    studentIdColumnLabel = Label(teacherAppointmentFrame,text="Student ID",font='helvitika 8 bold')
    studentIdColumnLabel.place(x=290,y=180)

    #Student Appointment Frame Code:
    studentAppointmentFrame = Frame(root, width=400, height=600)
    #studentAppointmentFrame.place(x=0,y=0)

    studentAppointmentFrameLabel = Label(studentAppointmentFrame, text="Your Appointments", fg="#e74c3c",
                                         font=helvitika)
    studentAppointmentFrameLabel.place(x=110, y=50)

    yourIdColumnLabel = Label(studentAppointmentFrame, text="Your ID", font='helvitika 8 bold')
    yourIdColumnLabel.place(x=50, y=180)

    dateColumnLabel = Label(studentAppointmentFrame, text="Date", font='helvitika 8 bold')
    dateColumnLabel.place(x=210, y=180)

    timeColumnLabel = Label(studentAppointmentFrame, text="Time", font='helvitika 8 bold')
    timeColumnLabel.place(x=130, y=180)

    facultyIdColumnLabel = Label(studentAppointmentFrame, text="Faculty ID", font='helvitika 8 bold')
    facultyIdColumnLabel.place(x=290, y=180)


    #Student Book Appointments Frame code:
    studentBookAppointmentFrame = Frame(root, width=400, height=600)
    #studentBookAppointmentFrame.place(x=0, y=0)

    #Adding label , button , input feilds in Student Book Appointments Frame
    facultytIdLabel = Label(studentBookAppointmentFrame,text="Faculty ID :",font=helvitika)
    facultytIdLabel.place(x=50,y=100)

    facultytIdInput = Entry(studentBookAppointmentFrame,font=helvitika)
    facultytIdInput.place(x=50, y=140, width=300, height=30)

    appointmentDateLabel = Label(studentBookAppointmentFrame,text="Date :",font=helvitika)
    appointmentDateLabel.place(x=50,y=200)

    appointmentDatePicker = DateEntry(studentBookAppointmentFrame,selectmode='day')
    appointmentDatePicker.place(x=50, y=240, width=300, height=30)

    timePickerLable = Label(studentBookAppointmentFrame,text="Pick a Time from 9.00 to 19.00",font=helvitika)
    timePickerLable.place(x=50,y=300)

    timePickerInput = Entry(studentBookAppointmentFrame,font=helvitika)
    timePickerInput.place(x=50, y=340, width=300, height=30)

    submitBtn = Button(studentBookAppointmentFrame,text="Book",bg="#2ecc71",fg="#ffffff",font=helvitika,
                       command= lambda: addappointment(studentId))
    submitBtn.place(x=100, y=400, width=220, height=40)

    studentBookAppointmentFrameBackBtn = Button(studentBookAppointmentFrame,text="Back",bg='red',fg='white',
                                                command=backtostudentBookingFrame)
    studentBookAppointmentFrameBackBtn.place(x=0,y=0)

    root.mainloop()

def showteacherLoginframe():
    teacherLoginFrame.pack(fill='both',expand=1)
    firstFrame.forget()

def showteacherBookingsFrame():
    global emplyeeId
    auth=authentication()
    try:
        teacher_test = auth.authenticate_employee(teacherIdInput.get(), departmentInput.get())
        emplyeeId = teacher_test[0]
        teacherLoginFrame.forget()
        teacherBookingsFrame.pack(fill='both',expand=1)
    except Exception as e:
        messagebox.showerror("Invalid Input","INVALID INPUT")
        print('pai nai')


def showstudentLoginFrame():
    firstFrame.forget()
    studentLoginFrame.pack(fill='both',expand=1)

def showstudentBookingFrame():
    global studentId
    auth=authentication()
    try:
        student_test = auth.authenticate_student(studentIdInput.get(),sectionInput.get(), departmentInput_student.get())
        # print(student_test)
        studentId = student_test[0]
        #print(studentId)
        studentLoginFrame.forget()
        studentBookingFrame.pack(fill='both',expand=1)
    except Exception as e:
        messagebox.showerror("invalid input","INVALID INPUT")

def showstudentBookAppointmentFrame():
    studentBookAppointmentFrame.pack(fill='both',expand=1)
    studentBookingFrame.forget()

def backtowelcome():
    firstFrame.pack(fill='both',expand=1)
    studentLoginFrame.forget()
    teacherLoginFrame.forget()

def backtoteacherlogin():
    teacherLoginFrame.pack(fill='both',expand=1)
    teacherBookingsFrame.forget()

def backtostudentlogin():
    studentLoginFrame.pack(fill='both',expand=1)
    studentBookingFrame.forget()


def backtostudentBookingFrame():
    studentBookAppointmentFrame.forget()
    studentBookingFrame.pack(fill='both',expand=1)


def addappointment(studentId):
    apntmnt = Appointment()
    try:
        facultuID = str(facultytIdInput.get())
        appointmentDate = str(appointmentDatePicker.get_date())
        time = str(timePickerInput.get())
        print(studentId)
        apntmnt.addAppointment(facultuID,appointmentDate,time
                                                  ,str(studentId))
        messagebox.showinfo("Appointment Added","Appointment Added")
    except Exception as e:
        print(e)
        print('pare nai')


def getAppountment(studentId):
    apntmnt = Appointment()
    try:
        response =  apntmnt.viewAppointmentData(studentId)
        print(response)
        if not len(response) == 0:
            left = 50
            top = 200
            for res in response:
                for r in reversed(list(res)):
                    newAppointmentInfo = Label(studentAppointmentFrame,text=r)
                    newAppointmentInfo.place(x=left,y=top)
                    left += 80
                top += 50
                left = 50
            studentAppointmentFrame.pack(fill='both',expand=1)
            studentBookingFrame.forget()
    except Exception as e:
        raise e

def getTeacherAppointments(emplyeeId):
    apntmnt = Appointment()
    try:
        response = apntmnt.viewTeacherAppointment(emplyeeId)
        if not len(response) == 0:
            left = 50
            top = 200
            for res in response:
                for r in res:
                    newAppointmentInfo = Label(teacherAppointmentFrame,text=r)
                    newAppointmentInfo.place(x=left,y=top)
                    left += 80
                top += 50
                left = 50
            teacherAppointmentFrame.pack(fill='both',expand=1)
            teacherBookingsFrame.forget()
    except Exception as e:
        raise e



