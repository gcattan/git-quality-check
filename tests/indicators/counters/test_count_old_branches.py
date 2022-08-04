from git_quality_check.indicators.counters import count_old_branches


def test():
    assert count_old_branches(["origin/gc/pytest_utils", "origin/update-readme"]) == 50
