def count_words(contents):
    words = contents.split()
    return len(words), words


def count_letters(words):
    letters = {}
    for word in words:
        lower_word = word.lower()
        for letter in lower_word:
            if letter in letters:
               letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


def sort_letters(letters_dict):
    letter_list = []
    for letter in letters_dict:
        if letter.isalpha():
            temp_dict = {
                    "letter": letter,
                    "count": letters_dict[letter],
            }
            letter_list.append(temp_dict)

    def sort_on(dict):
        return dict["count"]

    letter_list.sort(reverse=True, key=sort_on)

    return(letter_list)


def generate_report(location, word_count, letters):
    print(f"--- Begin report of {location} ---")
    print(f"{word_count} words found in the document\n")

    for letter in letters:
        print(f"The '{letter['letter']}' was found {letter['count']} times")

    print("--- End report ---")


def main():
    location = "books/frankenstein.txt"
    with open(location) as file:
        file_contents = file.read()
    count, words = count_words(file_contents)
    letter_count = count_letters(words)
    letters_sorted = sort_letters(letter_count)
    generate_report(location, count, letters_sorted)


if __name__ == "__main__":
    main()
