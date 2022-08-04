import subprocess
import sys
from datetime import datetime
from .common import get_date, diff_month, strip


def is_valid_log(log: str):
    return not log == ""


def run_git(command: list[str]):
    command.insert(0, "--no-pager")
    command.insert(0, "git")
    return subprocess.check_output(command).decode()


def git_logs():
    return run_git(["log"]).split("commit ")


def is_old(branch):
    branch_date = git_get_branch_date(branch)
    if not branch_date:
        return False
    date = get_date()
    return diff_month(date, branch_date) > 2


def git_all_branches():
    ret = run_git(["branch", "-r"]).split("\n")
    return [strip(r) for r in ret if not strip(r) == ""]


# checks if branchA contains branchB
def contains(branchA: str, branchB: str):
    if not is_well_formed_branch(branchA) or not is_well_formed_branch(branchB):
        return False
    if branchA == branchB:
        return False
    try:
        ret = run_git(["branch", "--contains", branchB, "-r"]).split("\n")
        print(ret)
    except:
        print("Git `branch --contains failed with: ", branchB)
        return False
    for r in ret:
        if branchA == r.strip().lstrip():
            return True
    return False


def is_well_formed_branch(branch: str):
    return not "->" in branch


def git_get_branch_date(branch: str):
    if not is_well_formed_branch(branch):
        return None
    ret = run_git(["log", "-n", "1", '--date=format:"%Y-%m-%d"', branch, "-r"]).split(
        "Date: "
    )[1]
    ret = ret.replace('"', "").split("-")
    year = int(strip(ret[0]))
    month = int(ret[1])
    day = int(ret[2].split("\n")[0])
    return datetime(year, month, day)


def remove_first_line(log: str):
    if is_valid_log(log):
        try:
            eol = log.index("\n")
            log = log[eol + 1 :]
        except ValueError:
            # commit is empty or just contains one line
            return ""
    return log


def remove_header(log: str):
    log = remove_first_line(log)  # Hash
    log = remove_first_line(log)  # Author
    log = remove_first_line(log)  # Date
    return log
