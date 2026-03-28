# Write your solution here
def shortest(words):
    short = len(words[0])
    short_word = words[0]
    for item in words:
        if len(item) < short:
            short = len(item)
            short_word = item
    return short_word    

if __name__ == "__main__":
    print(shortest(['ada','kathleen','comsmo']))