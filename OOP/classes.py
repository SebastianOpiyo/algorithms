class Student:
    """This is a student blueprint, from which we we instantiate/create students
    objects.
    - This is a simple into to classes in python."""

    # Constructor Method
    def __init__(self, name=None, department=None, admission_num=None):
        self.name = name
        self.department = department
        self.admission_num = admission_num

    # Define other methods below
    def get_student_details(self):
        print("Enter your name")
        self.name = input()
        print("Enter your department")
        self.department = input()
        print("Enter your admission number")
        self.admission_num = input()

    def print_student_info(self):
        print("Student's details:")
        print("Name: ", self.name)
        print("Department: ", self.department)
        print("Admission Number: ", self.admission_num)


# The first student object
student1 = Student()
student1.get_student_details()
student1.print_student_info()

# The second student object
student2 = Student()
student2.get_student_details()
student2.print_student_info()