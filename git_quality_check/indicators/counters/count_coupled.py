from git_quality_check.utils import sample, contains


def count_coupled(branches, main_branches):
    branches, count = sample(branches, 10)
    branches.extend(main_branches)
    count += len(main_branches)
    counter = 0
    max_counter = 0
    for bA in branches:
        for bB in branches:
            if not bA == bB:
                print(bA, bB, contains(bA, bB) )
                counter += 1 if contains(bA, bB) else 0
                max_counter += 1
    return counter / max_counter * 100
