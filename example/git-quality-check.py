from git_quality_check.utils import (
    git_logs,
    git_all_branches,
    set_output,
    format_number,
    parse_inputs,
)

from git_quality_check.indicators.counters import (
    count_old_branches,
    count_coupled,
    process_logs,
)


from git_quality_check.indicators.commits import (
    is_empty_body,
    not_a_squashed_commit,
    does_contain_bad_words,
    is_test_commit,
)

from git_quality_check.scoring import compute_score


if __name__ == "__main__":

    bad_words, main_branches = parse_inputs()

    logs = git_logs()
    branches = git_all_branches()

    bad_commit_index = process_logs(
        logs, [not_a_squashed_commit, is_empty_body, does_contain_bad_words(bad_words)]
    )
    test_index = process_logs(logs, [is_test_commit])

    old_branches_index = count_old_branches(branches)
    coupling_index = count_coupled(branches, main_branches)

    print("Percent of bad commits: ", format_number(bad_commit_index))
    print("Percent of test commits: ", format_number(test_index))
    print("Percent of old branches: ", format_number(old_branches_index))
    print("Percent of coupled branches", format_number(coupling_index))

    overall = compute_score(
        bad_commit_index, test_index, old_branches_index, coupling_index
    )

    set_output(format_number(overall))
