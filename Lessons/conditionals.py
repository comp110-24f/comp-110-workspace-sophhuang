"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big mumber!")
    print("Have a nice day!")


less_than_10(num=5)


def should_i_eat(hungry: bool) -> None:
    """Tels me whether or not to eat based on hunger."""
    if hungry:
        print("Eat some food!")  # "then" block
    else:
        print("Do your Comp110 homework instead.")  # "else" block
    print("I'm proud of you <3")  # either way, be kind to yourself


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))


def get_weather_report() -> str:
    """Display weather instructions."""
    weather: str = input("What is the weather?")
    if weather == "rainy" or "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
