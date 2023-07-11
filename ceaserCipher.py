def ceaserCipher(msg, n):
    """Returns msg shifted by n letters in alphabet"""
    result = ""
    for char in msg:
        char = char + 4
        result += char
    return result

print(ceaserCipher('Hello', 3))
        