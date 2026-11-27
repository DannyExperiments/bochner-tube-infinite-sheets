"""Exact rational checks of the polynomial and geometric margins."""
from fractions import Fraction as F


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


a = F(1, 10)
assert 1 - F(1, 4) == F(3, 4)
assert 2 - a * F(9, 4) > 0
assert F(41, 40) < 3
assert F(6, 5)**2 < 3**2
assert 3**2 - F(1, 40)**2 > 1
assert 3 < 4

# A connector-inequality fixture for m, K, delta.
m, K, delta = F(1, 20), F(6, 5), F(1, 100)
assert 0 < delta < min(F(1, 40), m / (2 * (K + 1)))
assert K * delta < m / 2

for numerator in range(-60, 61):
    t = F(numerator, 19)
    x = (1 - t*t) / (1 + t*t)
    y = 2*t / (1 + t*t)
    assert x*x + y*y == 1
    z1, z2 = (1 + a*x, 0), (a*y, 1)
    polynomial = add(mul(z1, z1), mul(z2, z2))
    factorized = mul((a*x, a*y), (2 + a*x, -a*y))
    assert polynomial == factorized
    assert 2 + a*x > 0

assert add(mul((F(11, 10), 0), (F(11, 10), 0)), (-1, 0)) == (F(21, 100), 0)
print("PASS: 121 exact circle fixtures, polynomial value, connector and exterior margins.")
