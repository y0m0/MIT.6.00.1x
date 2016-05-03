def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    chypertext = ""
    
    for letter in text:
        if letter not in coder:
            chypertext += letter
        else:
            chypertext += coder[letter]

    return chypertext
