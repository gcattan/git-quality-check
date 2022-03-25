from re import L
import subprocess
from datetime import datetime
import random

bad_words = ["WIP", "work in progress", "in progress", "TODO"]
main_branches = ["origin/develop", "origin/master"]

def run_git(command:list[str]):
    command.insert(0, "--no-pager")
    command.insert(0, "git")
    return subprocess.check_output(command).decode()

def git_logs():
    return run_git(["log"]).split("commit ")

def remove_first_line(log:str):
    if is_valid_log:
        try:
            eol = log.index("\n")
            log = log[eol+1:]
        except ValueError:
            #commit is empty or just contains one line
            return "" 
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

def remove_header(log:str):
    log = remove_first_line(log) # Hash
    log = remove_first_line(log) # Author
    log = remove_first_line(log) # Date
    return log

def is_empty_body(log:str):
    if not is_valid_log(log):
        return 1
    log = remove_header(log)
    if not is_valid_log(log):
         return 1
    return 0

####################################
def not_a_squashed_commit(log):
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

####################################

def strip(s:str):
    return s.strip().lstrip()

def git_all_branches():
    ret = run_git(["branch", "-r"]).split("\n")
    return [strip(r) for r in ret]

def git_get_branch_date(branch):
    if "->" in branch:
        return None
    ret = run_git(["log", "-n", "1", "--pretty=%as", branch]).split("-")
    return datetime(int(ret[0]), int(ret[1]), int(ret[2]))

def get_date():
    return datetime.today()

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

def is_old(branch):
    branch_date = git_get_branch_date(branch)
    if not branch_date:
        return False
    date = get_date()
    return diff_month(date, branch_date) > 2

def sample(l:list[str], min:int):
    count = len(l)
    if(count > min):
        l = random.sample(branches, min)
        count = min
    return (l, count)

def count_old_branches(branches):
    counter = 0
    branches, count = sample(branches, 10)
    for branch in branches:
        counter += 1 if is_old(branch) else 0
    return counter / count * 100

def are_coupled(branchA:str, branchB:str):
    if branchA == branchB:
        return False
    ret = run_git(["branch", "--contains", branchA, "-r"]).split("\n")
    for r in ret:
        if branchB == r.strip().lstrip():
            return True
    return False


def count_coupled(branches):
    branches, count = sample(branches, 10)
    branches.extend(main_branches)
    count += len(main_branches)
    counter = 0
    for bA in branches:
        for bB in branches:
            counter = 1 if are_coupled(bA, bB) else 0
    return counter / count * 100

logs = git_logs()
branches = git_all_branches()

bad_commit_index = process_logs(logs, [not_a_squashed_commit, is_empty_body, count_bad_words])
test_index = process_logs(logs, [is_test_commit])

old_branches_index = count_old_branches(branches)
coupling_index = count_coupled(branches)


print(bad_commit_index)
print(test_index)
print(old_branches_index)
print(coupling_index)

# bad_commit_index = 0
# test_index = 100
# old_branches = 0
# coupling = 0

overall = (100 - bad_commit_index) + \
 test_index + (100 - old_branches_index) + \
     (100 - coupling_index)

print(overall / 4)

