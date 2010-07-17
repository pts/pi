#! /usr/bin/python

import sys

def arcctg(x, u):
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
  while v >= 10:
    a = 1
    pa = 10
    b = 1
    pb = 10
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
  ys = str(4 * (4 * arcctg(5, u) - arcctg(239, u)))
  c = numdigits(maxerr(digits)))
  while ys[-c] == '0':
    c += 1
  return '3.' + ys[1 : -c]

print pi(5)
