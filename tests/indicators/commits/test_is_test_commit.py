import pytest
from git_quality_check.indicators.commits import is_test_commit


@pytest.mark.parametrize("log", ["test", "testing", "test it", "I am testing it"])
def test_is_test_commit(log):
    assert is_test_commit(log) == 1


def test_is_not_test_commit():
    log = """Tset"""
    assert is_test_commit(log) == 0
