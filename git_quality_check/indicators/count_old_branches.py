from git_quality_check.utils import (
    sample,
    is_old
)

def count_old_branches(branches):
    counter = 0
    branches, count = sample(branches, 10)
    for branch in branches:
        counter += 1 if is_old(branch) else 0
    return counter / count * 100