# write your solution here
def largest():
    max_num = 0
    with open("numbers.txt") as numbers:
        for value in numbers:
            value = int(value)
            if value > max_num:
                max_num = value
    return(max_num)

if __name__ == "__main__":
    largest()