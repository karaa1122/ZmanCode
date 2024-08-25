
def translate_to_kurish(kurish_code):
    
    mapping = {
        "agar": "if",
        "agareki_tr": "elif",
        "agar_na": "else",
        "chap": "print",
        "lo": "for",
        "ka": "while",
    }

    words = kurish_code.split()
    python_code = []

    for word in words:
        python_code.append(mapping.get(word, word))

        if word in words:
            python_code.append(word)
        
    return " ".join(python_code)
