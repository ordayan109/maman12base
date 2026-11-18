from dataclasses import dataclass
from time import perf_counter_ns


@dataclass(frozen=True)
class Result:
    values: list[int]
    comparisons: int
    writes: int
    nanoseconds: int


class _Q:
    __slots__ = ("c", "w")

    def __init__(self):
        self.c = 0
        self.w = 0


def _a(x, q):
    for i in range(1, len(x)):
        v, j = x[i], i - 1
        while j >= 0:
            q.c += 1
            if x[j] <= v:
                break
            x[j + 1] = x[j]
            q.w += 1
            j -= 1
        x[j + 1] = v
        q.w += 1


def _b(x, q):
    n = len(x)
    for i in range(n - 1):
        z = i
        for j in range(i + 1, n):
            q.c += 1
            if x[j] < x[z]:
                z = j
        if z != i:
            x[i], x[z] = x[z], x[i]
            q.w += 2


def _c0(x, y, p, r, q):
    if r - p < 2:
        return
    m = (p + r) // 2
    _c0(x, y, p, m, q)
    _c0(x, y, m, r, q)
    i, j, k = p, m, p
    while i < m and j < r:
        q.c += 1
        if x[i] <= x[j]:
            y[k] = x[i]
            i += 1
        else:
            y[k] = x[j]
            j += 1
        q.w += 1
        k += 1
    while i < m:
        y[k] = x[i]
        q.w += 1
        i += 1
        k += 1
    while j < r:
        y[k] = x[j]
        q.w += 1
        j += 1
        k += 1
    for k in range(p, r):
        x[k] = y[k]
        q.w += 1


def _c(x, q):
    _c0(x, [0] * len(x), 0, len(x), q)


def _d0(x, n, i, q):
    while True:
        z = i
        l = 2 * i + 1
        r = l + 1
        if l < n:
            q.c += 1
            if x[l] > x[z]:
                z = l
        if r < n:
            q.c += 1
            if x[r] > x[z]:
                z = r
        if z == i:
            return
        x[i], x[z] = x[z], x[i]
        q.w += 2
        i = z


def _d(x, q):
    n = len(x)
    for i in range(n // 2 - 1, -1, -1):
        _d0(x, n, i, q)
    for r in range(n - 1, 0, -1):
        x[0], x[r] = x[r], x[0]
        q.w += 2
        _d0(x, r, 0, q)


def run(algorithm, values):
    k = str(algorithm).upper()
    f = {"A": _a, "B": _b, "C": _c, "D": _d}.get(k)
    if f is None:
        raise ValueError("algorithm must be A, B, C, or D")
    x = list(values)
    q = _Q()
    t = perf_counter_ns()
    f(x, q)
    t = perf_counter_ns() - t
    return Result(x, q.c, q.w, t)
