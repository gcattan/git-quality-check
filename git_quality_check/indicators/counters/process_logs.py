def process_logs(logs: list[str], functions: list[str:int]):
    """
        Call a list of functions on the commit logs.
        Each function is a scoring function that returns
        either 1 or 0.
        The method then return the percent of functions having returned 1.

    >>>>>>> d427c6eba7617351a44a3bf759bdb38e9b3ce25d
        Parameters
        ----------
        logs: list[str]
            The commit logs
        functions: list[str:int]
            A list of scoring functions, taking a commit log as a parameter
            and returning either 1 or 0.
            Note, it is expected that all scoring functions have the same `meaning`.
            That is, they all return 1 (or 0) when the logs is validated (or unvalidated).

        Returns
         -------
        percent: float
            The percent of functions having returned 1.
    """
    counter = 0
    count = len(logs) * len(functions)
    for i in range(len(logs)):
        log = logs[i]
        for function in functions:
            # a same commit can be marked twice if it fails two functions
            counter += function(log)
    return counter / count * 100
