book = "frankenstein.txt"
with open("books/{}".format(book)) as f:
    file_contents = f.read()
    count = file_contents.split()

def count_word_frequency(file_contents):
    word_count = {}
    for word in file_contents.split():
        if word.lower() not in word_count:
            word_count[word.lower()] = 1
        else:
            word_count[word.lower()] += 1
    for word, count in word_count.items():
        if count > 50:
            print(word, count)

def count_letter_frequency(file_contents):
    letter_count = {}
    letterList = []
    for letter in file_contents:
        if letter.lower() not in letter_count:
            letter_count[letter.lower()] = 1
            letterList.append(letter.lower())
        else:
            letter_count[letter.lower()] += 1
    letterList.sort()
    for letter in letterList:
        if letter.isalpha():
            print("The '{0}' character was found {1} times".format(letter, letter_count[letter]))

print("--- Begin report of books/{0} ---\n{1} words found in the book\n".format(book,len(count)))
count_letter_frequency(file_contents)
print("\nA little bonus: most common words in the book:\n")
count_word_frequency(file_contents)
print("\n--- End report of books/frankenstein.txt ---")

