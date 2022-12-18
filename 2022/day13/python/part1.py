"""TODO"""
import itertools
from typing import Any, List, Tuple, Union


def parse(lines: List[str]) -> List[Tuple[List[Any], List[Any]]]:
    """TODO"""
    result: List[Tuple[List[Any], List[Any]]] = []
    tmp1: List[Any] = []
    tmp2: List[Any] = []
    for line in lines:
        if line.strip() == "":
            result.append((tmp1, tmp2))
        else:
            tmp1 = tmp2
            tmp2 = eval(line)  # pylint: disable=eval-used

    result.append((tmp1, tmp2))
    return result


def compare(  # pylint: disable=too-many-return-statements
    left: Union[int, None, List[Any]], right: Union[int, None, List[Any]]
) -> int:
    """TODO"""
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if left > right:
            return 1
        return 0

    if isinstance(left, list) and isinstance(right, list):
        for left_item, right_item in itertools.zip_longest(left, right):
            if (result := compare(left_item, right_item)) != 0:
                return result
        return 0

    left = [left] if isinstance(left, int) else left
    right = [right] if isinstance(right, int) else right
    return compare(left, right)


def compute_answer(lines: List[str]) -> int:
    """TODO"""
    result = 0
    pairs = parse(lines)
    for index, (left, right) in enumerate(pairs):
        if compare(left, right) != 1:
            result = result + (index + 1)

    return result
