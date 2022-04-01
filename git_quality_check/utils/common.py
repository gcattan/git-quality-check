
import random
import os
from datetime import datetime


def parse_inputs():
    bad_words = []
    main_branches = []
    try:
        bad_words = os.environ["INPUT_BADWORDS"].split(", ")
    except:
        bad_words = ["WIP", "work in progress", "in progress", "TODO"]
    try:
        main_branches = os.environ["INPUT_MAINBRANCHES"].split(", ")
    except:
        main_branches = ["origin/develop", "origin/master"]
    return bad_words, main_branches

def strip(s: str):
    return s.strip().lstrip()

def get_date():
    return datetime.today()

def sample(li: list[str], min: int):
    count = len(li)
    if(count > min):
        li = random.sample(li, min)
        count = min
    return (li, count)

def format_number(number:float):
    return "{0:.2f}".format(number)

def set_output(output:str):
    print(f"::set-output name=score::{output}")

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


