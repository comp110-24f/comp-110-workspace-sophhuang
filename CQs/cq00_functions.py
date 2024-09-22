"""The first challenge question"""

__author__ = "730653485"


def mimic(message: str) -> str:
    """Return message back to you"""
    return message


def main() -> None:
    """print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
