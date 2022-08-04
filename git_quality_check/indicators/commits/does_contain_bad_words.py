def does_contain_bad_words(bad_words: list[str]):
    def _does_contain_bad_words(log: str):
        counter = 0
        for word in bad_words:
            if word.lower() in log.lower().split():
                counter += 1
        return 1 if counter > 0 else 0

    return _does_contain_bad_words
