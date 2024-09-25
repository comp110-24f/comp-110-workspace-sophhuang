"""Searches for a letter in a five letter word and tell you the index location and total amount of occurances."""

__author__: str = "730653485"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if (
        len(word) != 5
    ):  # this will allow me to print the message for any length of word that isn't 5 letters.
        print("Error: Word must contain 5 characters.")
        exit()
        # this location makes sense because it lets the phrase above still print but won't return anything. It also is in the then block so it will only exit if the word inputted isn't 5 characters.
    return word  # regardless of if the conditional for the if function is true or not, it will always return the word back to me.


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    occurrence: int = (
        0  # before counting, the amount of matching characters should be at zero.
    )
    if (
        len(word) == 5 and len(letter) == 1
    ):  # I want to make sure that the rest of the code runs for only when the length of the word and letter inputted are correct.
        if letter == word[0]:
            print(letter + " found at index 0")
            occurrence = (
                occurrence + 1
            )  # because the if function being true means that there was a match, so the count should increase by one.
        if letter == word[1]:
            print(letter + " found at index 1")
            occurrence = occurrence + 1
        if letter == word[2]:
            print(letter + " found at index 2")
            occurrence = occurrence + 1
        if letter == word[3]:
            print(letter + " found at index 3")
            occurrence = occurrence + 1
        if letter == word[4]:
            print(letter + " found at index 4")
            occurrence = occurrence + 1
    if (
        occurrence == 0
    ):  # if there were none, I want it to print "no instances" rather than "0 instances"
        print("No instances of" + letter + " found in " + word)
    elif (
        occurrence == 1
    ):  # I realized that instance shouldn't be plural if there was one match found.
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(occurrence) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
