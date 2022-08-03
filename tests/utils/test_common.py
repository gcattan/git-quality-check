import os
from git_quality_check.utils.common import (
    BADWORDS,
    MAINBRANCHES,
    parse_inputs,
    sample,
    diff_month,
)
from datetime import datetime


def test_parse_inputs():
    os.environ[BADWORDS] = "WIP, todo"
    os.environ[MAINBRANCHES] = "origin/develop, origin/main"
    bad_words, main_branches = parse_inputs()
    assert bad_words[0] == "WIP"
    assert bad_words[1] == "todo"
    assert main_branches[0] == "origin/develop"
    assert main_branches[1] == "origin/main"


def test_sample_same_size_than_list():
    li = [3, 10, 6, 15, 20]
    size = len(li)
    sample_list, count = sample(li, size)
    assert count == size
    for i in range(size):
        assert li[i] == sample_list[i]


def test_sample_greater_size_than_list():
    li = [3, 10, 6, 15, 20]
    size = len(li)
    sample_list, count = sample(li, size + 1)
    assert count == size
    for i in range(size):
        assert li[i] == sample_list[i]


def test_sample_lower_size_than_list():
    li = [3, 10, 6, 15, 20]
    size = len(li) - 1
    sample_list, count = sample(li, size)
    assert count == size
    for i in range(size):
        assert sample_list[i] in li


def test_diff_months():
    date1 = datetime("2022", "08", "01")
    date2 = datetime("2023", "08", "01")
    assert diff_month(date1, date2) == 12
    assert diff_month(date2, date1) == 12
