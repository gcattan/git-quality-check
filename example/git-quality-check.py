from git_quality_check.utils import (
    git_logs,
    git_all_branches,
    set_output,
    format_number,
    parse_inputs,
    add_safe_directory,
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

    add_safe_directory()
    logs = git_logs()
    branches = git_all_branches()

    bad_commit_index = process_logs(
        logs, [not_a_squashed_commit, is_empty_body, does_contain_bad_words(bad_words)]
    )
    test_index = process_logs(logs, [is_test_commit])

    old_branches_index = count_old_branches(branches)
    coupling_index = count_coupled(branches, main_branches)

    print("Percent of bad commits: ", format_number(bad_commit_index))
    print(
        "    A high number of bad commits means you should avoid WIP or empty commits for example."
    )
    print("Percent of test commits: ", format_number(test_index))
    print(
        "    A low number of test commits, might indicates that you are not writing enough tests for your software."
    )
    print("Percent of old branches: ", format_number(old_branches_index))
    print(
        "    A high percent of old branches, means that you should delete unused branches or already merged branches in your repo."
    )
    print("Percent of coupled branches", format_number(coupling_index))
    print(
        "    A high percent of coupled branches, means that you should use more often squash \
        and merge and avoid upmerge of your master/main branch in feature branches.\
        A high number of coupled branches complicate your commit history and make difficult the use of git-bisect for example."
    )

    overall = compute_score(
        bad_commit_index, test_index, old_branches_index, coupling_index
    )

    set_output(format_number(overall))
