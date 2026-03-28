# Write your solution here
def everything_reversed(array):
    result = []
    for item in array:
        result.insert(0,item[::-1])
    return result

if __name__ == "__main__":
    print(everything_reversed(["Hi", "there", "example", "one more"]))