"""Practice with questions on gradescope lessons"""


def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx <= len(msg):
        print(msg[idx])
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"
chars(msg=a)
print(copy)  # can't print it because it's a local variable under the function char
