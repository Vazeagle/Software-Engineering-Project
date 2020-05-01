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
    def __init__(self, name, direction, orientations, school, sp_lessons, departments):
        self.name = name
        self.direction = direction
        self.orientations = orientations
        self.departments = departments
        self.school = school
        self.sp_lessons = sp_lessons

class School:
    def __init__(self, name):
        self.name = name