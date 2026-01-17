import string
def preprocess_texts(statements):
    processed_list = []
    for text in statements:
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = text.split()
        processed_list.append(tokens)
    return processed_list