# write your solution here
if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

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
        grades[parts[0]] = total

for uid, name in names.items():
    if uid in grades:
        total = grades[uid]
        print(f"{name} {total}")
    else:
        continue
