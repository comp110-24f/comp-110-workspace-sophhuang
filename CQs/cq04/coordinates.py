"""Importing challenge question"""

__author__ = "730653485"


def get_coords(xs: str, ys: str) -> None:
    xx = 0  # index for xs
    while xx < len(xs):
        yy = 0  # index for ys
        while yy < len(ys):
            print("(" + xs[xx] + "," + ys[yy] + ")")
            yy += 1
        xx += 1
