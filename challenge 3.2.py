"""
Implement a function called sort students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll number (string), and capa (float). Test the function with different input lists of students. 
"""

class Student:

 def __init__(self, name,roll_number, cgpa): 
   self.name=name
   self.roll_number = roll_number
   self.cgpa=cgpa

def sort_students (student_list):
#sort the list of students indescending order-of-egpa 
   sorted_students = sorted(student_list, key=lambda student:student.cgpa, reverse = True)

   return sorted_students


#example usage:
students = [Student("Vino", "A123",7.8), Student("Sherin", "A122", 8.9), Student("Anu", "A120", 9.2), Student("Nithu", "A121", 9.6)]

sorted_students =sort_students (students)

#print the sorted list of students

for student in sorted_students: 
  print("Name: {}, Roll Number: {}, cgpa: {}".format(student.name, student.roll_number, student.cgpa))