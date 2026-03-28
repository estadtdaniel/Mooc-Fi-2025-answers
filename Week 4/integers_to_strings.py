# Write your solution here
def formatted(array):
    array_f = []
    for item in array:
        num = f"{item:.2f}"
        array_f.append(num)
    return array_f
        

if __name__ == "__main__":
    formatted([1.234, 0.3333, 0.11111, 3.446])
    print(formatted([1.234, 0.3333, 0.11111, 3.446]))