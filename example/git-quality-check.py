import os
from git_quality_check.utils import (
    git_logs,
    git_all_branches,
    set_output,
    format_number
)

from git_quality_check.indicators.counters import (
    count_old_branches,
    count_coupled,
    process_logs
)

from git_quality_check.indicators.commits import (
    is_empty_body,
    not_a_squashed_commit,
    count_bad_words,
    is_test_commit,
    bad_words
)

global main_branches


def compute_score(bad_commit_index, test_index,
                  old_branches_index, coupling_index):
    return ((100 - bad_commit_index) +
            test_index + (100 - old_branches_index) +
            (100 - coupling_index))/4


def parse_inputs():
    global bad_words, main_branches
    try:
        bad_words = os.environ["INPUT_BADWORDS"].split(", ")
    except:
        bad_words = ["WIP", "work in progress", "in progress", "TODO"]
    try:
        main_branches = os.environ["INPUT_MAINBRANCHES"].split(", ")
    except:
        main_branches = ["origin/develop", "origin/master"]


if __name__ == "__main__":

    parse_inputs()

    logs = git_logs()
    branches = git_all_branches()

    bad_commit_index = process_logs(logs, [not_a_squashed_commit,
                                        is_empty_body,
                                        count_bad_words])
    test_index = process_logs(logs, [is_test_commit])

    old_branches_index = count_old_branches(branches)
    coupling_index = count_coupled(branches, main_branches)
    
    print(bad_commit_index)
    print(test_index)
    print(old_branches_index)
    print(coupling_index)



    overall = compute_score(bad_commit_index, test_index,
                            old_branches_index, coupling_index)

    set_output(format_number(overall))