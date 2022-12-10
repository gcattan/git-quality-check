from git_quality_check.utils import (
    is_valid_log,
    remove_header,
)


def is_empty_body(log: str):
    """
    Return true if the body of the commit is empty.
    (not taking into account the headers).

    Parameters
    ----------
    log : str
        The log of a commit.

    Returns
     -------
    is_empty: Bool
        true if the body of the commit is empty.
    """
    if not is_valid_log(log):
        return 1
    log = remove_header(log)
    if not is_valid_log(log):
        return 1
    return 0
