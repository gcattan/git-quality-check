def is_test_commit(log: str):
    for word in ["test", "testing"]:
        if word in log.lower().split():
            return 1
    return 0