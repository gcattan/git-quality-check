def not_a_squashed_commit(log: str):
    if "(#" not in log:
        return 1
    return 0