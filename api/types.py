# https://fastapi.tiangolo.com/python-types/
# more bout types

def add(first:str , last:str):
    # specify karna ki ye string hai
    return first+" "+ last

first = "saatvik"
last = "srivastava"
# this is type checking
print(add(first.capitalize(),last))
