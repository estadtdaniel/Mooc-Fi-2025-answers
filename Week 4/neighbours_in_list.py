# Write your solution here
def longest_series_of_neighbours(array):
    count = 1 
    max_count = 1
    num = array[0]
    array = array[1:]
    for item in array:
        if (num-1) == item or (num+1) == item:
            num = item
            count +=1
        else:
            num = item
            if max_count < count:
                max_count = count
            count = 1
        print(f"{count},{item},{max_count}")

    if max_count < count:
        max_count = count
        print(f"{count},{item}")
    return max_count

if __name__ == "__main__":
    my_list = [1, 2, 3, 0, 1, 2, 3, 4, 5, 3, 4, 5, 1, 2, 3]
    print(longest_series_of_neighbours(my_list))