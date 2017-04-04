def compress_str(str):

    count = 0
    compressed_str = ''
    letter = str[0]

    for char in str:
        if char == letter:
            count += 1
        elif char != letter:
            compressed_str = compressed_str + (letter + str(count))
            letter = char
            count = 1

    if len(compressed_str) >= len(str):
        return str

    return compressed_str

compress_str('aabcccccaaa')