class Lesson:
    def __init__(self, name):
        self.name = name

class Direction:
    def __init__(self, name, lessons):
        self.name = name
        self.lessons = lessons

class Orientation:
    def __init__(self, name, direction, lesson):
        self.name = name
        self.direction = direction
        self.lesson = lesson

class Department:
    def __init__(self, name, orientations):
        self.name = name
        self.orientations = orientations
        
class Student:
    def __init__(self,id, name, direction, orientations, school, sp_lessons, departments):
        self.name = name
        self.id = id
        self.direction = direction
        self.orientations = orientations
        self.departments = departments
        self.school = school
        self.sp_lessons = sp_lessons

class School:
    def __init__(self, name):
        self.name = name

class Application:
    def __init__(self,student,data,status):
        self.student = student
        self.status = status
        self.data = data

class Seatsapp:
    def __init__(self,department,rseats,fseats,reasoning,file):
        self.department = department
        self.rseats = rseats
        self.fseats = fseats
        self.reasoning = reasoning
        self.file = file
class Board:
    def __init__(self, seatsDue,list,examCal):
        self.seatsDue = seatsDue
        self.list = list
        self.examCal = examCal

class Cal:
    def __init__(self,events):
        self.events = events

class calEvent:
    def __init__(self,date,reminder,message):
        self.date = date
        self.reminder = reminder
        self.message = message