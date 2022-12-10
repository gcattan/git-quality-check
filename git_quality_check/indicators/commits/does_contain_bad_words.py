def does_contain_bad_words(bad_words: list[str]):
    """
    Factory method returning an handler that tell if a log contains
    the specified bad words.

    Parameters
    ----------
    bad_words : list[str]
        A list of word to be avoided in a commit log.

    Returns
     -------
    _does_contain_bad_words: Callable(log: str)
        Handler method that return 1 if the log contains the specified
        "bad" words (0 otherwise)
    """

    def _does_contain_bad_words(log: str):
        counter = 0
        for word in bad_words:
            if word.lower() in log.lower().split():
                counter += 1
        return 1 if counter > 0 else 0

    return _does_contain_bad_words
