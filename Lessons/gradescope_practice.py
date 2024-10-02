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
# chars(msg=a)
# print(copy)  # can't print it because it's a local variable under the function char


"""LS14"""

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
