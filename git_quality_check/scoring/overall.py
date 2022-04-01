def compute_score(bad_commit_index, test_index,
                  old_branches_index, coupling_index):
    return ((100 - bad_commit_index) +
            test_index + (100 - old_branches_index) +
            (100 - coupling_index))/4