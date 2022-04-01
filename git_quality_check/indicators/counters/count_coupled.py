from git_quality_check.utils import sample, are_coupled

def count_coupled(branches, main_branches):
    branches, count = sample(branches, 10)
    branches.extend(main_branches)
    count += len(main_branches)
    counter = 0
    for bA in branches:
        for bB in branches:
            counter += 1 if are_coupled(bA, bB) else 0
    return counter / count * 100