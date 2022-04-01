bad_words: list[str] = []

def count_bad_words(log: str):
    counter = 0
    for word in bad_words:
        if word in log.lower().split():
            counter += 1
    return counter