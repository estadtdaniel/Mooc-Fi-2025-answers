# Write your solution here
def list_sum(num1,num2):
    i = 0
    total = [0]*len(num1)
    while i<len(num1):
        total[i] = num1[i]+num2[i]
        i+=1
    return total    

if __name__ == "__main__":
    total = list_sum([1,2,3],[1,2,3])
    print(total)