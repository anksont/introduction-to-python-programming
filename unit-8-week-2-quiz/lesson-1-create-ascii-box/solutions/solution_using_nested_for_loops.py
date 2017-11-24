def create_box(height, width, character):
    result = ''
    for h in range(height):
        line = ''
        for w in range(width):
            line += character
        result += (line + '\n')
    return result
