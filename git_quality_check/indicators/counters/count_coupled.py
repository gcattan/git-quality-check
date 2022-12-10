from git_quality_check.utils import sample, contains


def count_coupled(branches: list[str], main_branches: list[str]):
    """
    Returns the percent of coupled branches.
    A branch is coupled to another branch if it is contained
    in this other branch history (git branch --contains...).
    When there is more than 10 branches, the method randomly
    selects 10 branches among all branches plus the branches
    passed through the `main_branches` input.

    Parameters
    ----------
    branches : list[str]
        The branches in the git repository.
    main_branches: list[str]
        Additional branches to look into.
        This is useful when the number of branche is > 10.
        In this case, the method randomly
        selects 10 branches among all branches plus the branches
        passed through the `main_branches` input.

    Returns
     -------
    percent: float
        The percent of coupled branches
        (or an estimation in cases where the number of branches is > 10)
    """
    branches, count = sample(branches, 10)
    branches.extend(main_branches)
    count += len(main_branches)
    counter = 0
    max_counter = 0
    for bA in branches:
        for bB in branches:
            if not bA == bB:
                counter += 1 if contains(bA, bB) else 0
                max_counter += 1
    return counter / max_counter * 100
