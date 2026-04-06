import time as pytime
"""
source of __builtin__ functions
"""

__builtins_funcs__ = [
    ["_time", []],
    ["_sleep", ["ms"]]
]


def _time():
    """return time in ns"""
    return pytime.time_ns()

def _wait(ms):
    return pytime.sleep(ms) 