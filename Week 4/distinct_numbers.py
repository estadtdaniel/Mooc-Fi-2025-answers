# create an array with only distinct numbers
def distinct_numbers(num):
    num.sort()
    new_num = []
    new_num.append(num[0])
    for i in range(1,len(num),1):
        if num[i] != num[i-1]:
            new_num.append(num[i])
    return(new_num)
    

if __name__ == "__main__":
    num = distinct_numbers([5,2,2,5,2,5,3,0])
    print(num)