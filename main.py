with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def word_counter(book):
    words = book.split()
    num_words = len(words)
    return num_words

def letter_counter(book):
    your_dict = {}
    letters = str(list(book.split()))
    for letter in letters.lower():
        if letter in your_dict:
            your_dict[letter] += 1
        else:
            your_dict[letter] = 1
    return your_dict

def summary_bot(book):
    print("--Begin Report of Book {f}")
    print(f"There are {word_counter(file_contents)} in this book")
    dicto = dict(sorted(letter_counter(file_contents).items(), key=lambda item: item[-1]))
    keys = list(dicto.keys())
    values = list(dicto.values())
    for i in range(0, len(values)):
        print(f"There are {values[i]} instances of {keys[i]} in this book")

summary_bot(file_contents)

