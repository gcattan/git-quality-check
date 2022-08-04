import pytest
from git_quality_check.indicators.commits import is_empty_body

@pytest.mark.parametrize(
        'log', ['', 'commit 1234455']
    )
def test_is_empty_body(log):
    assert is_empty_body(log) == 1


def test_is_not_empty_body():
    log = """commit 7a1e2a6a76e6967bde14e95900996ca17811de47 (origin/gc/pytest)
    Author: gcattan <gregoire.cattan@ibm.com>
    Date:   2022-04-17
    remove dependencies"""
    assert is_empty_body(log) == 0
