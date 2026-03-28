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

        total = 0 
        for grade in parts[1:]:
            total += int(grade)
        percent = int((total/40)*10)
        grades[parts[0]] = []
        grades[parts[0]].append(total)
        grades[parts[0]].append(percent)

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

name = "name"
exec_nbr = "exec_nbr"
exec_pts = "exec_pts."
exm_pts ="exm_pts."
tot_pts = "tot_pts."
grade = "grade"

print(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}")

for key,name in names.items():
    if key in grades:
        total_exercise = grades[key][1]
    if key in exams:
        total_exams = exams[key]
    course_total = total_exercise + total_exams
    course_grade[key] = []
    course_grade[key].append(course_total)
    if course_total <= 14:
        course_grade[key].append(0)
    elif course_total > 14 and course_total <= 17:
        course_grade[key].append(1)
    elif course_total > 17 and course_total <= 20:
        course_grade[key].append(2)
    elif course_total > 20 and course_total <= 23:
        course_grade[key].append(3)
    elif course_total > 23 and course_total <= 27:
        course_grade[key].append(4)
    elif course_total > 27:
        course_grade[key].append(5)
    #course_grade[key][0] = total points
    #course_grade[key][1] = final grade
    #exams[key] = exam grade
    #grades[key][0] = total exercises
    #grades[key][1] = exercise points
    print(f"{names[key]:30}{grades[key][0]:<10}{grades[key][1]:<10}{exams[key]:<10}{course_grade[key][0]:<10}{course_grade[key][1]:<10}")


