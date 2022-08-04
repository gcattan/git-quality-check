import pytest
from datetime import datetime
from git_quality_check.utils.git import (
    is_old,
    git_all_branches,
    contains,
    git_get_branch_date,
    remove_first_line,
)


def test_branch_is_old():
    assert is_old("origin/gc/pytest") == True
    assert is_old("origin/gc/pytest_utils") == False


def test_branch_contains():
    assert contains("origin/gc/test-action", "origin/gc/pytest") == False
    assert contains("origin/master", "origin/formatter") == True


def test_git_all_branches():
    branches = git_all_branches()
    assert len(branches) > 0
    assert "origin/master" in branches


def test_git_get_branch_date():
    date = git_get_branch_date("origin/formatter")
    assert date == datetime(2022, 4, 1)


def test_remove_first_line():
    commit = """commit 7a1e2a6a76e6967bde14e95900996ca17811de47 (origin/gc/pytest)
    Author: gcattan <gregoire.cattan@ibm.com>
    Date:   2022-04-17
    remove dependencies"""
    commit = remove_first_line(commit)
    commit = remove_first_line(commit)
    commit = remove_first_line(commit)
    assert commit == "    remove dependencies"
    commit = remove_first_line(commit)
    assert commit == ""
    commit = remove_first_line(commit)
    assert commit == ""
