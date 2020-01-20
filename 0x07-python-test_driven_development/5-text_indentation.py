#!/usr/bin/python3
def text_indentation(text):
    """function that prints a text with 2 new lines after each of these characters:"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for n in range(len(text)):
        if text[n - 1] in ",?:":
            continue
        print(text[i], end=" ")
        if text[i] in ".?:":
            print("\n")
