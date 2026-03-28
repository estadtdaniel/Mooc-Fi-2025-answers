# Write your solution here
def sum_of_positives(num):
    sum = 0
    
    for i in num:
        if i > 0:
            sum = sum + i
    return sum 

if __name__ == "__main__":
    num = [1,-1,5,4]
    result = sum_of_positives(num)
    print(f"The result is {result}")