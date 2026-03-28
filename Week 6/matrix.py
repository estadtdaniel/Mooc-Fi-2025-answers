# write your solution here
def matrix_sum():
    with open("matrix.txt") as matrix:
        total = 0
        for line in matrix:
            num = line.split(",")
            sum_num = 0 
            for value in num:
                value = int(value)
                sum_num += value
            total += sum_num
    return total

def matrix_max():
    with open("matrix.txt") as matrix:
        max_num = 0
        for line in matrix:
            num = line.split(",")
            for value in num:
                if int(value) > max_num:
                    max_num = int(value)
    return max_num

def row_sums():
    with open("matrix.txt") as matrix:
        array = []
        for line in matrix:
            num = line.split(",")
            sum_num = 0 
            for value in num:
                value = int(value)
                sum_num += value
            array.append(sum_num)
    return array


if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()
