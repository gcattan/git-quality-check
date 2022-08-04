from git_quality_check.indicators.commits import does_contain_bad_words


def test():
    bad_words = ["bad", "word"]
    counter = does_contain_bad_words(bad_words)
    log = "I am a very bad bad word"
    assert counter(log) == 1
    log = "I am a good log"
    assert counter(log) == 0
