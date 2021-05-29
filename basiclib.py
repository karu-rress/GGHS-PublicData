from typing import Dict, List
from functools import singledispatch

"""

@singledispatch
def func(x):
    pass

@func.register(List)
def _(x):
    pass

...

"""


class otd:

    @staticmethod
    def rm_duplicate(lt: List) -> List:
        return list(set(lt))

    @staticmethod
    def sort_dict(dict: Dict, is_ascending: bool=True) -> Dict:
        if is_ascending:
            return {k: v for k, v in sorted(dict.items(), key=lambda item:-item[1])}
        else:
            return {k: v for k, v in sorted(dict.items(), key=lambda item:item[1])}
    """
    @staticmethod
    def new_list() -> List:
        return []
    """

