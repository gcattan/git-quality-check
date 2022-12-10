def not_a_squashed_commit(log: str):
    """
    Return true if the commit is not a squashed commit.
    (ie. it was not squased and merged from a PR).

    Parameters
    ----------
    log: str
        The log of a commit.

    Returns
     -------
    is_not_a_squashed_commit: int
        1 if the commit is NOT a squashed commit (0 otherwise).
    """
    if "(#" not in log:
        return 1
    return 0
