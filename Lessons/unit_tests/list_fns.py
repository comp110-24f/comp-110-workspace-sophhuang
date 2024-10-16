def get_first(input: list[str]) -> str:
    """Return first elements."""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Remove first element from input."""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Removed and returns first element."""
    x: str = input[0]
    input.pop(0)
    return x
