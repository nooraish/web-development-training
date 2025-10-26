# Global variable
students = []
def add_student(name, age, grade):
    global students
    student = {
        "name" : name,
        "age"  : age,
        "grade" :grade
    }
    students.append(student)
    print(f"added{name}")

def display_student():
    if len(students) == 0:
        print("no student found")
        return
    print("\nStudent List :")
    for i, student in enumerate(students, 1):
        print(f" {i}.{student['name']} , GRADE : {student['grade']}, Age: {student['age']}")


def get_grade_stats():
    if len(students) == 0:
        print("No students to analyze!")
        return

    grade_count = {}
    for student in students:
        grade = student['grade']
        if grade in grade_count:
            grade_count[grade] += 1
        else:
            grade_count[grade] = 1

    print("\nGrade Statistics:")
    for grade, count in grade_count.items():
        print(f"  Grade {grade}: {count} student(s)")

def get_grade_A():
    print("list of students with grade A")
    for student in students:
        if student['grade'] == 'A':
            print(f"{student['name']}")




add_student("aisha",10,"A")
add_student("abi", 10, "A")
add_student("test", 10, "B")
display_student()
get_grade_stats()
get_grade_A()


