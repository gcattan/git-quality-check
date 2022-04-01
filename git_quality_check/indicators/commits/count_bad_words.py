def count_bad_words(bad_words: list[str]):
    def _count_bad_words(log: str):
        counter = 0
        for word in bad_words:
            if word in log.lower().split():
                counter += 1
        return counter
    return _count_bad_words