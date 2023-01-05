#!/usr/bin/python3
"print text with 2 new lines afte separators"


def text_indentation(text):
    """Print text with new lines after seperator.
    Args:
        text: The text to scan
    Raises:
        TypeError: if text is not a string.
    """
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while (i < len(text)):
        print(text[i], end='')
        if text[i] == '\n' or text[i] in ".?:":
            if text[i] in ".?:":
                print('\n')
            i += 1
            while (i < len(text) and text[i] == ' '):
                i += 1
            continue
        i += 1
