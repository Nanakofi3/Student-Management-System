# Creating a student management system


# Base class for a Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")



# inherits from Person (Child class for a Student)
class Student(Person):
    def __init__(self, student_id, name, age, grade):
        super().__init__(name, age) 
        self.student_id = student_id
        self.grade = grade

    # Polymorphism: overriding display_info()
    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


# Management system
class StudentMgtSys:

    def __init__(self):
        self.students = {}  

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Error: Student ID already exists.")
            return
        
        if not isinstance(age, int) or age <= 15:
            print("Error: Invalid age")
            return
        
        if grade not in ['A', 'B', 'C', 'D', 'F']:
            print("Error: Invalid grade")
            return

        self.students[student_id] = Student(student_id, name, age, grade)
        print(f"{name} has been added successfully!")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student {student_id} removed successfully!")
        else:
            print("Error: Student ID not found.")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return
        print("\nStudent Records:")
        for student in self.students.values():
            student.display_info()  # Polymorphism in action!

    def find_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print("\nStudent Found:")
            student.display_info()
        else:
            print("Error: Student ID not found.")


# Main program
if __name__ == "__main__":
    sms = StudentMgtSys()

    sms.add_student(123, "Grace", 24, "B")
    sms.add_student(123, "Grace", 24, "B")
    sms.add_student(124, "John", 16, "C")
    sms.add_student(125, "Nana", 24, "A")
    sms.add_student(126, "Kay", 24, "D")

    sms.display_students()

    sms.find_student(125)
    sms.find_student(254)
    
    sms.remove_student(123)
    sms.remove_student(255)
