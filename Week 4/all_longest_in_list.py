# Write your solution here
def all_the_longest(words):
    long = len(words[0])
    long_word = []
    for item in words:
        if len(item) > long:
            long = len(item)

    for item in words: 
        if len(item) == long:
            long_word.append(item)
    return long_word    

if __name__ == "__main__":
    print(all_the_longest(['ada','kathleen','cosmo','max','eric1234']))