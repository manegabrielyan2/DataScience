student_grades = {
    'Alice':88,
    'Bob' : 6,
    'Charlie':1,
    'Diana':85,
    'Evan':92,
    'Fiona':11,
    'George':95
}
def average_grade(student_grades):
    """
    This function counts the average grade.
    """
    length = len(student_grades)
    average = 0
    for i in student_grades.keys():
        average += i
    average /= length
    return average

def highest_grade(student_grades):
    """
    This functions finds student with highest grade.
    
    """
    maxx = 0
    for i in student_grades:
        if student_grades[i] > maxx:
            maxx = student_grades[i]
    for i in student_grades:
        if student_grades[i] == maxx:
            print(f'{i} has the highest grade with {student_grades[i]} points.')
    
def lowest_grade(student_grades):
    """
    This functions finds student with lowest grade.
    
    """
    minn = 0
    for i in student_grades:
        if student_grades[i] < minn:
            minn = student_grades[i]
    for i in student_grades:
        if student_grades[i] == minn:
            print(f'{i} has the lowest grade with {student_grades[i]} points.')

def pass_fail(students_grades):
    """
    This function seperates students into two groups: 
    those who failed and those who passed.
    """
    passs = []
    fail = []
    for name , grade in students_grades.items():
        if grade < 75:
            fail.append(name)
            print(f'{name} failed with {grade} scores.')
        else:
            passs.append(name)
            print(f'{name} passed with {grade} scores.')
    print(f'following students failed:{fail}')
    print(f"Following students passed the test:{passs}")
# pass_fail(student_grades)

def improvement(student_grades):
    """
    This function is for messaging students to take tutoring sessions.
    Prints the messege when grade is less than 85.
    """
    for name , grade in student_grades.items():
        if grade < 85:
            print(f'{name}, we suggest you take tutoring sessions to improve your skills.')
# improvement(student_grades)
def text_bar_chart(student_grades):
    """
    This function is aimed to print a chart with stars 
    corresponding to student's grade
    """
    for name , grade in student_grades.items():
        if grade % 10 >= 5:
            print(f'{name}: {"*" * ((grade//10) + 1)}')
        else:
            print(f'{name}: {"*" * (grade//10)}')
text_bar_chart(student_grades)

# highest_grade(student_grades)
# lowest_grade(student_grades)
