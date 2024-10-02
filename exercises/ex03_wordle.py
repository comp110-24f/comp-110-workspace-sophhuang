"""My own wordle!"""

__author__: str = "730653485"


def input_guess(secret_word_len: int) -> str:
    word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        # the while loop will have it keep looping back and asking to try again if the length of the input word doesn't match the secret word length
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """search for the character guessed in the secret word"""
    assert len(char_guess) == 1
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Compare two strings to equal length and give back the emojis associated with wordle"""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    output: str = ""
    # made this output variable to be able to add on boxes to the string as we got through the index
    while idx < len(secret_word):
        if user_guess[idx] == secret_word[idx]:  # this means the letters match up
            output += GREEN_BOX
            idx += 1
        elif contains_char(secret_word=secret_word, char_guess=user_guess[idx]) is True:
            # the elif allows it to go into the box if the above function box was false, and having the function contains_char be true indicates a yellow box.
            output += YELLOW_BOX
            idx += 1
        else:  # for when the letters don't match up AND the letter isn't in the secret word anywhere
            output += WHITE_BOX
            idx += 1
    return output


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    attempts: int = 1
    # keeps track of the attempts until it reaches 6 so the program can exit the while loop
    while attempts <= 6:
        print(f"=== Turn {attempts}/6 ===")
        guess_user: str = input_guess(
            secret_word_len=len(secret)
        )  # I created another variable equal to the guess so I could assign it as an argument to the parameter user_guess for function emojified
        print(emojified(user_guess=guess_user, secret_word=secret))
        if guess_user == secret:
            print(f"You won in {attempts}/6 turns!")
            return None  # this return line will have the program exit the function box if the word is guessed correctly
        attempts += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
