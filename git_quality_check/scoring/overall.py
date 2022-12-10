def compute_score(
    bad_commit_index: int, test_index: int, old_branches_index: int, coupling_index: int
):
    """
    Compute a global score based on four different indices.
    The closer to 100%, the higher the quality.

    Parameters
    ----------
    bad_commit_index: list[str]
        the percent of commits containg a list of prohibited words.
        Count negatively.
    test_index: list[str]
        the percent of commits related to testing.
        Count postively.
    old_branches_index: list[str]
        Count negatively.
    coupling_index: list[str]
        Count negatively.

    Returns
    -------
    global_score: float
        The overall score.

    See Also
    --------
    git_quality_check.indicators.commits.does_contain_bad_words
    git_quality_check.indicators.commits.is_test_commit
    git_quality_check.indicators.counters.count_old_branches
    git_quality_check.indicators.counters.count_coupled
    """
    return (
        (100 - bad_commit_index)
        + test_index
        + (100 - old_branches_index)
        + (100 - coupling_index)
    ) / 4
