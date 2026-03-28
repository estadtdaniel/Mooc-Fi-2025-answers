# Write your solution here
def length_of_longest(array):
    big = len(array[0])
    for item in array:
        if len(item) > big:
            big = len(item)
    return big

if __name__ == "__main__":
    print(length_of_longest(['ada','kathleen','comsmo']))
