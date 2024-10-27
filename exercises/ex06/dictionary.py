"""Dictionary utility funcitons exercise"""

__author__: str = "730653485"


def invert(input: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    # made a new dictionary I can assign the inverted keys and values
    for key in input:
        new_key: str = input[key]
        # I made a new variable for the inverted key and assigned it to the value from the original dictionary
        if new_key in inverted_dict:
            # if true, that means that the new key already exists in the inverted dictionary so I need to raise the KeyError
            raise KeyError("There are multiple copies of values in your dictionary!")
        inverted_dict[new_key] = key
    return inverted_dict


def favorite_color(FC_input: dict[str, str]) -> str:
    color_count: dict[str, int] = {}
    # made a separate dictionary that can keep track of the frequency a color occurs
    for names in FC_input:
        color = FC_input[names]
        if color in color_count:
            # if the color is already a key in the dictionary, I just have to increase the value by one
            color_count[color] += 1
        else:
            # if the color isn't in the dictionary, I add it as a key with the value set at 1
            color_count[color] = 1
    most_popular_color: str = ""
    # made a string variable I can assign the name of the color with the most counts to
    max_num: int = 0
    # I figured out that I need a integer variable of the current highest number found in the for in loop to make the comparison of less or greater than to the value in my color_count dictionary so I can make those if then statements
    for color in color_count:
        count: int = color_count[color]
        if max_num < count:
            max_num = count
            most_popular_color = color
    return most_popular_color


def count(values_list: list[str]) -> dict[str, int]:
    counter: dict[str, int] = {}
    for value in values_list:
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1
    return counter


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    alpha: dict[str, list[str]] = {}
    for word in words:
        first_letter: str = word[0].lower()
        if first_letter in alpha:
            alpha[first_letter].append(word)
            # this adds the word to the list within the dictionary associated with the key of the first letter
        else:
            alpha[first_letter] = []
            # if the first letter isn't in the dictionary yet as a key, I need to add it as a key first. Then I can add the word to the list as a value
            alpha[first_letter].append(word)
    return alpha


def update_attendance(
    attendance_form: dict[str, list[str]], weekday: str, student: str
) -> None:
    if weekday in attendance_form:
        if student not in attendance_form[weekday]:
            attendance_form[weekday].append(student)
    elif weekday not in attendance_form:
        attendance_form[weekday] = []
        attendance_form[weekday].append(student)
