"""
FINDING THE KEY
"""

from typing import TextIO  # Specific annotations


def decrypt(input_file: TextIO, wordlist_filename: str) -> str:
    """
    Using wordlist_filename, decrypt input_file according to the handout
    instructions, and return the plaintext.
    """
    # TODO write your code
    pass


if __name__ == "__main__":

    # Sample input from the handout -- you can tweak this if you like
    print(decrypt(open("book1.txt"), "wordlist.txt"))
