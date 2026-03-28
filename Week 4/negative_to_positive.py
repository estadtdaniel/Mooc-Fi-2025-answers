# Write your solution here
num = int(input("Please type in a positive integer:"))
num_neg = num*-1
for i in range(num_neg,num+1,1):
    if i == 0:
        continue
    print(i)