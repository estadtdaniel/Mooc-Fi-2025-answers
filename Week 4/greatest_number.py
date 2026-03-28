def greatest_number(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    elif n3>=n2 and n3>=n1:
        return n3
    else:
        return n1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest)