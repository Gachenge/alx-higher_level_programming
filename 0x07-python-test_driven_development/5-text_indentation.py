#!/usr/bin/python3
"print text with 2 new lines afte separators"


def text_indentation(text):
    """Print text with new lines after seperator.
    Args:
        text: The text to scan
    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] == '\n' or text[i] in '.?:':
            print('\n')
