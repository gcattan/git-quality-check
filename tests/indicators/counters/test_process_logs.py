from git_quality_check.indicators.counters import process_logs
from git_quality_check.indicators.commits import not_a_squashed_commit, is_empty_body


def test():
    logs = [
        """Commit 1234
    Author: 
    Date:
    Test""",
        """Commit 1234
    Author: 
    Date:
    Merge (#5)""",
        "",
    ]
    marked_commits = process_logs(logs, [not_a_squashed_commit, is_empty_body])
    assert marked_commits == 50
