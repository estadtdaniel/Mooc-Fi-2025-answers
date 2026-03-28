# Write your solution here
def add_student(student:dict,name:str):
    student[name] = {}
def print_student(student:dict,name:str):
    total = 0
    if name not in student:
        print(f"{name}: no such person in the database")
        return
    else:
        print(f"{name}:")
        if len(student[name][1]) == 0:
            print(" no completed courses")
        else:
            count = len(student[name][1])
            for item in student[name][1]:
                if item[0] == 0:
                    count -= 1
                else:
                    continue
            print(f" {count} completed courses:")
    
            for item in student[name][1]:
                if item[0] == 0:
                    continue
                else:
                    print(f"  {item[0]} {item[1]}")
                    total += item[1]
            
            print(f" average grade {total/count}")
def add_course(student:dict, name:str, course:tuple):
    course_name = course[0]
    score = course[1]
    
    if score != 0:
        course = (course_name,score)
        if len(student[name][1]) > 0:
            for i in range(0,len(student[name][1]),1):
                if course_name == student[name][1][i][0]:
                    if score > student[name][1][i][1]:
                        replace = i
                        student[name][1][replace] = (0,0)
                    elif score < student[name][1][i][1]:
                        break
                    else:
                        i += 1
            else:
                student[name][1].append(course)
        else:
            student[name][1].append(course)
    return course
def summary(student:dict):
    num_students = len(student) #number of students
    max_count = 0
    student_HS = []
    
    
    for key,value in student.items():
        if len(value[1]) > max_count:
            max_count = len(value[1]) #most completed courses
            max_student = key #student with most completed
        
        total = 0
        length = 0
        for item in student[key][1]:
            if item[0] == 0:
                continue
            else:
                total += item[1]
                length += 1
        student_HS.append((key,total/length))
    
    highest_avg = 0
    for item in student_HS:
        if item[1] > highest_avg:
            highest_avg_student = item[0]
            highest_avg = item[1]
    print(f"students {num_students}")
    print(f"most courses completed {max_count} {max_student}")
    print(f"best average grade {highest_avg} {highest_avg_student}")

        
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 4))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    summary(students)
