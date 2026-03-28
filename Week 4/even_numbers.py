# Write your solution here
def even_numbers(num):
    num_even=[]

    for i in num:
        if i%2 == 0:
            num_even.append(i)
    return num_even 

if __name__ == "__main__":
    num = [1,6,5,4]
    result = even_numbers(num)
    print(f"The result is {result}")