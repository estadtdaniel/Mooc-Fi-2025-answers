# Write your solution here
def most_common_character(array):
    char = []
    for item in array:
        if char.count(item) != 1:
            char.append(item)
    big = 0
    for item in char:
        if array.count(item) > big:
            big = array.count(item)
            big_char = item

    return big_char


if __name__ == "__main__":
    print(most_common_character('aabbbbc'))
