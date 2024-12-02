import hashlib


def hash_starts_with(number: int, secret_key: str, starts_with='00000') -> int:
    string_to_hash = secret_key + str(number)
    hashed = hashlib.md5(str(string_to_hash).encode('utf-8')).hexdigest()
    return hashed.startswith(starts_with)


def question_one(data: str) -> int:
    res = 0
    while not hash_starts_with(res, data, '00000'):
        res += 1
    print(res)


def question_two(data: str) -> int:
    res = 0
    while not hash_starts_with(res, data, '000000'):
        res += 1
    print(res)



question_one("yzbqklnj")
question_two("yzbqklnj")