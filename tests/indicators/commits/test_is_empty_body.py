import pytest
from git_quality_check.indicators.commits import is_empty_body

@pytest.mark.parametrize(
        'log', ['', 'commit 1234455']
    )
def test_is_empty_body(log):
    assert is_empty_body(log) == 1


def test_is_not_empty_body():
    log = """commit 1234455
    Test"""
    assert is_empty_body(log) == 0
