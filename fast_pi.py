#! /usr/bin/python

import sys

def acot(x, u):
  sum = xpower = u // x
  xx = x * x
  n = 3
  while True:
    xpower //= xx
    term = xpower // n
    if not term:
      return sum
    sum -= term
    n += 2
    xpower //= xx
    term = xpower // n
    if not term:
      return sum
    sum += term
    n += 2

def maxerr(digits):
  return (286135312 * digits + 31739381 + 9999999) // 10000000

def numdigits(v):
  n = 1
  while v > 9:
    a = b = 1
    pa = pb = 10
    while v > pb:
      a = b
      pa = pb
      pb *= pb
      b *= 2
    v //= pa
    n += a
  return n

assert numdigits(0) == 1
assert numdigits(9) == 1
assert numdigits(10) == 2
assert numdigits(11) == 2
assert numdigits(99) == 2
assert numdigits(100) == 3
assert numdigits(101) == 3
assert numdigits(999) == 3
assert numdigits(1000) == 4
assert numdigits(1001) == 4
assert numdigits(9999) == 4
assert numdigits(10000) == 5
assert numdigits(47000) == 5
assert numdigits(10001) == 5
assert numdigits(99999) == 5
assert numdigits(100000) == 6
assert numdigits(100001) == 6

def pi(digits):
  """Return a string of at most ``digits'' characters, prefix of pi."""
  if digits < 3:
    return '3'
  u = 10 ** digits
  y = 4 * (4 * acot(5, u) - acot(239, u))
  y //= 10 ** (numdigits(maxerr(digits)) - 1)
  while y % 10 == 0:
    y //= 10
  return y // 10

assert pi(3) == 31
assert pi(35) == 3141592653589793238462643383279
assert pi(36) == 314159265358979323846264338327950
assert pi(37) == 3141592653589793238462643383279502
assert pi(77) == 31415926535897932384626433832795028841971693993751058209749445923078164062
