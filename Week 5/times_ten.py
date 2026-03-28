# Write your solution here
def times_ten(start_index: int, end_index: int):
    index = {}
    item = start_index
    for item in range(start_index,end_index+1,1):
        index[item] = item * 10
    return index

if __name__ == "__main__":
    d = times_ten(4, 15)
    print(d)