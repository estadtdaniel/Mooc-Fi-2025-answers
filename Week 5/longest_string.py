# Write your solution here
def longest(strings: list):
    big = len(strings[0])
    big_item = strings[0]
    for item in strings:
        if len(item) > big:
            big = len(item)
            big_item = item

    return big_item


if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))
