# Write your solution here
def histogram(word:str):
    letter = {}
    for item in word:
        if item not in letter:
            letter[item] = 0
        letter[item] += 1
    
    for key in letter:
        d = letter[key]*"*"
        print(f"{key} {d}")

if __name__ == "__main__":
    print(histogram("aaateaaaaaa"))