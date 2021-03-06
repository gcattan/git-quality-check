from git_quality_check.utils import (
    is_valid_log,
    remove_header,
)


def is_empty_body(log: str):
    if not is_valid_log(log):
        return 1
    log = remove_header(log)
    if not is_valid_log(log):
        return 1
    return 0
