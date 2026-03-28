# Write your solution here
def double_items(numbers:list):
    number2 = []
    for item in numbers:
        number2.append(2*item)
    return number2


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)