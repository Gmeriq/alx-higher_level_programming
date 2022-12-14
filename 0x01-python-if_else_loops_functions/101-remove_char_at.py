#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = str
    output = ''
    index = 0
    for char in str1:
        if index == n:
            index += 1
            continue
        else:
            output += char
            index += 1
    return output
