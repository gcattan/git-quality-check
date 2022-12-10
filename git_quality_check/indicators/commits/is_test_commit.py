def is_test_commit(log: str):
    """
    Return true if the commit log contains
    "test" or "testing".

    Parameters
    ----------
    log : str
        The log of a commit.

    Returns
     -------
    is_test_commit: Bool
        true if the commit contains "test" or "testing". 
    """
    for word in ["test", "testing"]:
        if word in log.lower().split():
            return 1
    return 0
