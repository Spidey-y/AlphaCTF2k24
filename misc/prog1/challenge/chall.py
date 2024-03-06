#!/usr/bin/env python3

import numpy as np
import random
from sys import exit
from os import environ
from inputimeout import inputimeout


FLAG = environ.get("FLAG", "AlphaCTF{fake_flag_for_local_testing}")


def a(x: int, matrix: np.ndarray):
    matrix[1:9, x+0] = 1
    matrix[1:9, x+5] = 1
    matrix[0, x+1:x+5] = 1
    matrix[4, x+1:x+5] = 1


def b(x: int, matrix: np.ndarray):
    matrix[0:9, x+0] = 1
    matrix[0, x+1:x+5] = 1
    matrix[4, x+1:x+5] = 1
    matrix[8, x+1:x+5] = 1
    matrix[1:4, x+5] = 1
    matrix[5:8, x+5] = 1


def c(x: int, matrix: np.ndarray):
    matrix[1:8, x+0] = 1
    matrix[0, x+1:x+6] = 1
    matrix[8, x+1:x+6] = 1


def d(x: int, matrix: np.ndarray):
    matrix[0:9, x+0] = 1
    matrix[0, x+1:x+5] = 1
    matrix[8, x+1:x+5] = 1
    matrix[1:8, x+5] = 1


def e(x: int, matrix: np.ndarray):
    matrix[0:9, x+0] = 1
    matrix[0, x+1:x+6] = 1
    matrix[4, x+1:x+6] = 1
    matrix[8, x+1:x+6] = 1


def f(x: int, matrix: np.ndarray):
    matrix[0:9, x+0] = 1
    matrix[0, x+1:x+6] = 1
    matrix[4, x+1:x+6] = 1


def zero(x: int, matrix: np.ndarray):
    matrix[1:8, x+0] = 1
    matrix[0, x+1:x+5] = 1
    matrix[8, x+1:x+5] = 1
    matrix[1:8, x+5] = 1


def one(x: int, matrix: np.ndarray):
    matrix[0:9, x+0] = 1


def two(x: int, matrix: np.ndarray):
    matrix[0, x+0:x+6] = 1
    matrix[0:4, x+5] = 1
    matrix[4:9, x+0] = 1
    matrix[8, x+1:x+6] = 1
    matrix[4, x+1:x+6] = 1


def three(x: int, matrix: np.ndarray):
    matrix[0, x+0:x+6] = 1
    matrix[0:9, x+5] = 1
    matrix[8, x+0:x+6] = 1
    matrix[4, x+0:x+6] = 1


def four(x: int, matrix: np.ndarray):
    matrix[0:5, x+0] = 1
    matrix[4, x+0:x+6] = 1
    matrix[0:9, x+5] = 1


def five(x: int, matrix: np.ndarray):
    matrix[0, x+0:x+6] = 1
    matrix[0:4, x+0] = 1
    matrix[4:9, x+5] = 1
    matrix[8, x+0:x+6] = 1
    matrix[4, x+0:x+6] = 1


def six(x: int, matrix: np.ndarray):
    matrix[0, x+0:x+6] = 1
    matrix[0:9, x+0] = 1
    matrix[4:9, x+5] = 1
    matrix[8, x+0:x+6] = 1
    matrix[4, x+0:x+6] = 1


def seven(x: int, matrix: np.ndarray):
    matrix[0, x+0:x+6] = 1
    matrix[0, x+5] = 1
    matrix[1:9, x+5] = 1


def eight(x: int, matrix: np.ndarray):
    matrix[0:9, x+0] = 1
    matrix[0:9, x+5] = 1
    matrix[0, x+1:x+5] = 1
    matrix[4, x+1:x+5] = 1
    matrix[8, x+1:x+5] = 1


def nine(x: int, matrix: np.ndarray):
    matrix[0:5, x+0] = 1
    matrix[0:9, x+5] = 1
    matrix[0, x+1:x+5] = 1
    matrix[4, x+1:x+5] = 1
    matrix[8, x+0:x+5] = 1


chars = {
    "A": a,
    "B": b,
    "C": c,
    "D": d,
    "E": e,
    "F": f,
    "0": zero,
    "1": one,
    "2": two,
    "3": three,
    "4": four,
    "5": five,
    "6": six,
    "7": seven,
    "8": eight,
    "9": nine,
}


def solve(st: str):
    """
    This function takes a string as input and generates a matrix representation of the string.
    """
    # Create a matrix with appropriate dimensions
    matrix = np.zeros((9, 7*len(st)-1-(st.count("1")*5)-(st.count(" ")*5)))
    # Initialize the offset
    offset = 0
    # Iterate over each word in the string
    for word in st.split(" "):
        # Iterate over each character in the word
        for char in word:
            # Call the appropriate function based on the character
            chars[char](offset, matrix)
            # Update the offset based on the character
            if char == "1":
                offset += 2
            else:
                offset += 7
        # Add spacing between words
        offset += 2
    return matrix.tolist()


alphabet = "0123456789ABCDEF"
if __name__ == "__main__":
    for _ in range(100):
        phrase = " ".join(["".join(random.choices(alphabet, k=random.randint(3, 20)))
                           for _ in range(random.randint(3, 10))])
        try:
            ans = inputimeout(
                prompt=f"Enter the matrix for the following phrase: {phrase}\n>>> ", timeout=5)
        except:
            print("Too slow :(")
            exit()
        if all([c in "[,01 ]" for c in ans]):
            ans = eval(ans)
            assert isinstance(ans, list)
        else:
            print("Invalid input!")
            exit()
        sol = solve(phrase)
        if np.array_equal(ans, sol):
            print("Correct!")
        else:
            print("Incorrect!")
            exit()
    print("You did it!!!! here's your flag: ", FLAG)
    exit()
