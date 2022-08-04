def process_logs(logs: list[str], functions: list[str:int]):
    counter = 0
    count = len(logs) * len(functions)
    for i in range(len(logs)):
        log = logs[i]
        for function in functions:
            # a same commit can be marked twice if it failes two functions
            counter += function(log)
    return counter / count * 100
