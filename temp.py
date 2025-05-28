def vec(n: int, a: int) -> list[int]:
    return [int(i) for i in format(a, f'0{n}b')]


def int_v(n: int, a: list[int]) -> int:
    return int(''.join(map(str, a)), 2)


print(vec(8, 77))
print(int_v(8, vec(8, 77)))
