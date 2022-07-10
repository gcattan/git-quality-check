import random
import os
from datetime import date, datetime

BADWORDS = "INPUT_BADWORDS"
MAINBRANCHES = "INPUT_MAINBRANCHES"



def parse_inputs():
    """
    " Gets inputs from environment variables:
    " - bad_words: A list of words that should be avoided in commit messages.
    " - main_branches: The list of main branches (e.g. master, main or develop)
    """
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



def sample(li: list[str], n: int):
    """
    " Computes a sample of size 'n' from a list:
    " - if the size of the list is equal or lower than n, returns the list
    " - if the size of the list is greater than n, returns a sample of n.
    "   (some elements might be repetead)
    " 
    " li: the list
    " n: expected number of elements in the sample
    " 
    " Returns the tuple (sample, )
    """
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
