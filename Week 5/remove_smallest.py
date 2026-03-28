# Write your solution here
def remove_smallest(numbers:list):
    sorted_numbers = []
    for item in numbers:
        sorted_numbers.append(item)
    sorted_numbers.sort()
    small = sorted_numbers[0]

    numbers.remove(small)
    
    

if __name__ == "__main__":
    x = [2, 4, 6, 1, 3, 5,99,0]
    remove_smallest(x)
    print(x)