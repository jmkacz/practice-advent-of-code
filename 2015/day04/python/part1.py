import hashlib
from typing import List


def compute_answer(lines: List[str]) -> int:
    result = 1
    line = lines[0]
    while True:
        secret = (line + str(result)).encode()
        hash = hashlib.md5(secret).hexdigest()
        if hash[0:5] == "00000":
            return result
        result += 1
