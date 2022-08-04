from git_quality_check.scoring import compute_score


def test():
    assert compute_score(100, 0, 100, 100) == 0
    assert compute_score(0, 100, 0, 0) == 100
