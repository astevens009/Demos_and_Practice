student_name = ""       # global variable

class Starfleet_Student():
    global student_name
    count = 0
    def __init__(self, stflt_id = 2500, last_name = "Sisko", first_name = "Benjamin", 
                 rank = "Lieutenant"):
        Starfleet_Student.count += 1
        self.student_id = stflt_id
        self.last_name = last_name
        self.first_name = first_name
        self.rank = rank
        student_name = "{}, {}".format(self.last_name, self.first_name)

    def display_student_info(self):
        student_info = "{} {}, {}\n".format(self.rank, self.last_name, self.first_name)
        return student_info
    
    def get_student_id(self):
        return self.student_id
    
    def get_student_name(self):
        """
        Trying to modify a global variable
        """
        print("TEST: {}\n".format(student_name))
    
class StFlt_Course():
    def __init__(self, Starfleet_Student):
        self.enrollee = {}
    
    # Still need a hook to Starfleet_Student for each student instance
    # stflt_student = Starfleet_Student()
    # def __init__(self):
    #     self.enrollee = {}

    def add_student(self, Starfleet_Student):
        place = Starfleet_Student.get_student_id()
        self.enrollee[place] = Starfleet_Student
        


if __name__ == '__main__':
    new_student = Starfleet_Student(2501, "Dax", "Ezra")
    new_student2 = Starfleet_Student()  # using keywork args
    last_name = new_student.last_name
    first_name = new_student.first_name
    print("\nNew Student: {}, {}\n".format(last_name, first_name))

    # Keyword args
    print("{}".format(new_student2.display_student_info()))

    # Out of scope.
    print("Student Name: {}".format(student_name))

    # Retrieve global variable value
    new_student.get_student_name()
