from git_quality_check.indicators.counters import count_coupled


def test():
    assert count_coupled(["origin/update-readme"], ["origin/formatter"]) == 50
    assert count_coupled(["origin/test-action"], ["origin/formatter"]) == 0
