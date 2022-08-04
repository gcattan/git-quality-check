from git_quality_check.indicators.commits import not_a_squashed_commit


def test():
    assert not_a_squashed_commit("PR(#7)") == False
    assert not_a_squashed_commit("I am not squased") == True
