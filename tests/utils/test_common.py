import os
from git_quality_check.utils.common import (
    BADWORDS,
    MAINBRANCHES,
    parse_inputs
)

def test_parse_inputs():
    os.environ[BADWORDS] = 'WIP, todo'
    os.environ[MAINBRANCHES] = 'origin/develop, origin/main'
    bad_words, main_branches = parse_inputs()
    assert bad_words[0] == 'WIP'
    assert bad_words[1] == 'todo'
    assert main_branches[0] == 'origin/develop'
    assert main_branches[1] == 'origin/main'


def test_sample():
    assert False

def test_diff_months():
    assert False
