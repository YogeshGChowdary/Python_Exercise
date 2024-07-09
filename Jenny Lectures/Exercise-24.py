# Add new entry in student nested dictionary

student_data = [
    {
        'Name':'Ram',  # put comma after each key:value pair
        'roll_no':10,  # strings in quotes and integers no quote
        'age':20,
        'course':'python'
    },                     #put comma after each dictionary in list
    {
        'Name':'Ram',
        'roll_no':10,
        'age':20,
        'course':'python'
    }
]

def add_new_student(name,rollno,age,course_opted):
    new_student={}
    new_student['Name']=name
    new_student['roll_no'] =rollno
    new_student['age']=age
    new_student['course']=course_opted
    student_data.append(new_student)

add_new_student("Shyam",22,18,"C++")
#print(student_data)

#to print output each dicitonay in single line
for student in student_data:
  print(student)