# Write your solution here
def factorials(n: int):
    k = {}
    count = 0
    num = 1
    while count < n:
        count += 1
        num = num * count
        k[count] = num
    return k

if __name__ == "__main__":
    d = factorials(10)
    print(d[8])
        