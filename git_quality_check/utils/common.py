
from datetime import datetime
import random

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


