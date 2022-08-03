import pytest
from git_quality_check.utils.git import (
    is_old,
    git_all_branches,
    are_coupled,
    git_get_branch_date,
    remove_first_line,
)


def test_branch_is_old():
    assert is_old("origin/gc/pytest") == True
    assert is_old("origin/gc/pytest_utils") == False


def test_branch_are_coupled():
    assert True == False


def test_git_all_branches():
    assert True == False


def test_git_get_branch_date():
    assert True == False


def test_remove_first_line():
    assert True == False
