def print_upper_words(string):
    for word in string:
        print(word.upper())

print_upper_words(["hello", "world"])

def print_e_words(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)

print_e_words(["elementary", "estes", "figures", "leNoir"])

def must_start_with(words, letters):
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())
                break

must_start_with(["hello", "world","billy","bob","joe"], "b")