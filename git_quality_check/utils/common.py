import random
import os
from datetime import date, datetime

BADWORDS = "INPUT_BADWORDS"
MAINBRANCHES = "INPUT_MAINBRANCHES"


def parse_inputs():
    bad_words = []
    main_branches = []
    try:
        bad_words = os.environ[BADWORDS].split(", ")
    except:
        bad_words = ["WIP", "work in progress", "in progress", "TODO"]
    try:
        main_branches = os.environ[MAINBRANCHES].split(", ")
    except:
        main_branches = ["origin/develop", "origin/master"]
    return bad_words, main_branches


def strip(s: str):
    return s.strip().lstrip()


def get_date():
    return datetime.today()


# n: number of element to return in the sample
def sample(li: list[str], n: int):
    count = len(li)
    if count > n:
        li = random.sample(li, n)
        count = n
    return (li, count)


def format_number(number: float):
    return "{0:.2f}".format(number)


def set_output(output: str):
    print(f"::set-output name=score::{output}")


def diff_month(d1: date, d2: date):
    return (d1.year - d2.year) * 12 + d1.month - d2.month
