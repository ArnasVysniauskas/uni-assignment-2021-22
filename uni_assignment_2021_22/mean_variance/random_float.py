
from random import random


def randfloat(start: float, end: float) -> float:
    return random() * (end - start) + start
