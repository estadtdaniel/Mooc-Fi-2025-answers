# Write your solution here
def grade_input(num):
        num_split = num.split(" ")
        num_split = [int(x) for x in num_split]
        return num_split

def student_grade(array):

    if array[1] < 10:
        grade = 0 + array[0]
    elif array[1] >= 10 and array[1]<20:
        grade = 1 + array[0]
    elif array[1] >= 20 and array[1]<30:
        grade = 2 + array[0]
    elif array[1] >= 30 and array[1]<40:
        grade = 3 + array[0]
    elif array[1] >= 40 and array[1]<50:
        grade = 4 + array[0]
    elif array[1] >= 50 and array[1]<60:
        grade = 5 + array[0]
    elif array[1] >= 60 and array[1]<70:
        grade = 6 + array[0]
    elif array[1] >= 70 and array[1]<80:
        grade = 7 + array[0]
    elif array[1] >= 80 and array[1]<90:
        grade = 8 + array[0]
    elif array[1] >= 90 and array[1]<100:
        grade = 9 + array[0]
    elif array[1]==100:
        grade = 10 + array[0]
    return grade

def final_grade(point):
    if point < 14:
        result = 0
    elif point > 14 and point <=17:
        result = 1
    elif point > 17 and point <=20:
        result = 2
    elif point > 20 and point <=23:
        result = 3
    elif point > 23 and point <=27:
        result = 4
    elif point > 27 and point <=30:
        result = 5
    return result

def grade_distribution(grade_array):
    print("Grade distribution:")
    i=5
    while i >= 0:
        number = grade_array.count(i)
        print(f"    "+ f"{i}:"+" "+"*"*number)
        i-=1
    

def main ():
    count = 0
    total = 0
    result_array =[]
    while True:    
        num = input("Exam and exercises completed:")
        if num == "":
            break
        array = grade_input(num)
        grade = student_grade(array)
        total = total + grade 
        result = final_grade(grade)
        if array[0] < 10:
            result = 0
        result_array.append(result)
        count += 1
    mean = total/count
    print("Statistics:")
    print(f"Points average: {mean:.1f}")
    fail = result_array.count(0)
    pass_percentage = ((count - fail)/count)*100
    print(f"Pass percentage: {pass_percentage:.1f}")
    grade_distribution(result_array)
        
main ()