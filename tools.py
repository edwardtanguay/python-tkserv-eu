def uppercase_first_letter(text):
    if len(text) > 0:
        return text[0].upper() + text[1:]
    else:
        return text
