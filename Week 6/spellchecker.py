# write your solution here
text_input = input("Write: ").split()

for word in text_input:
    word_lower = word.lower()
    status = False
    with open("wordlist.txt") as file:
        for text in file:
            text = text.strip()
            if word_lower == text:
                status = True
                print(word, end=" ")
                break
        if status == False:
            print(f"*{word}*", end=" ")


