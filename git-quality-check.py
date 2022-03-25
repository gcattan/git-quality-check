import subprocess

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

#dead branch
#branch coupling


logs = git_logs()
quality_index = process_logs(logs, [no_squashed_commit, is_empty_body, count_bad_words])
test_index = process_logs(logs, [is_test_commit])

print(quality_index)
print(test_index)