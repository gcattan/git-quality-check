import subprocess
from datetime import datetime

bad_words = ["WIP", "work in progress", "in progress", "TODO"]
def git_logs():
    ret = subprocess.check_output(["git", "--no-pager", "log"]).decode()
    ret = ret.split("commit ")
    return ret

def remove_first_line(log:str):
    if(is_valid_log):
        try:
            eol = log.index("\n")
            log = log[eol+1:]
        except ValueError:
            return "" #commit is empty or just contains one line
    return log

def is_valid_log(log:str):
    return not log == ""

def process_logs(logs: list[str], functions: list[str: int]):
    counter = 0
    count = len(logs) * len(functions)
    for i in range(len(logs)):
        log = logs[i]
        for function in functions:
            counter += function(log)
    return counter / count * 100

def is_empty_body(log:str):
    if not is_valid_log(log):
        return 1
    log = remove_first_line(log) # Hash
    log = remove_first_line(log) # Author
    log = remove_first_line(log) # Date
    if not is_valid_log(log):
         return 1
    return 0

####################################
def no_squashed_commit(log):
    if not "(#" in log:
        return 1
    return 0

def count_bad_words(log:str):
    counter = 0
    for word in bad_words:
        if word in log.lower().split() :
            counter += 1
    return counter

def is_test_commit(log:str):
    for word in ["test", "testing"]:
        if word in log.lower().split():
            return 1
    return 0


# logs = git_logs()
# quality_index = process_logs(logs, [no_squashed_commit, is_empty_body, count_bad_words])
# test_index = process_logs(logs, [is_test_commit])

# print(quality_index)
# print(test_index)

####################################

def git_all_branches():
    ret = subprocess.check_output(["git", "--no-pager", "branch", "-r"]).decode()
    return [r.strip() for r in ret.splitlines()]

def git_get_branch_date(branch):
    if("->" in branch):
        return None
    ret = subprocess.check_output(["git", "log", "-n", "1", "--pretty=%as", branch]).decode()
    ret = ret.split("-")
    return datetime(int(ret[0]), int(ret[1]), int(ret[2]))

def get_date():
    # date = datetime.today().strftime('%Y-%m-%d')
    return datetime.today()

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def is_old(branch):
    branch_date = git_get_branch_date(branch)
    if not branch_date:
        return False
    date = get_date()
    return diff_month(date, branch_date) > 2

def count_old_branches(branches):
    count = len(branches)
    counter = 0
    for branch in branches:
        counter += 1 if is_old(branch) else 0
    return counter / count * 100



branches = git_all_branches()


print(count_old_branches(branches))
#dead branch
#branch coupling




