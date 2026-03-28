# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points= input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points= "exam_points1.csv"

names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] +" " + parts[2].strip()

grades = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue

        length = []

        for item in parts[1:]:
            length.append(int(item))
        total = 0 
        for grade in parts[1:]:
            total += int(grade)
        percent = int((total/40)*10)
        grades[parts[0]] = percent

exams = {}

with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        total = 0
        for exam_grade in parts[1:]:
            total += int(exam_grade)
        exams[parts[0]] = total

course_grade = {}

for key,name in names.items():
    if key in grades:
        total_exercise = grades[key]
    if key in exams:
        total_exams = exams[key]
    course_total = total_exercise + total_exams
    if course_total <= 14:
        print(f"{name} 0")
    elif course_total > 14 and course_total <= 17:
        print(f"{name} 1")
    elif course_total > 17 and course_total <= 20:
        print(f"{name} 2")
    elif course_total > 20 and course_total <= 23:
        print(f"{name} 3")
    elif course_total > 23 and course_total <= 27:
        print(f"{name} 4")
    elif course_total > 27:
        print(f"{name} 5")
