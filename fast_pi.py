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

def pi(digits):
  """Return a string of at most ``digits'' characters, prefix of pi."""
  if digits < 3:
    return '3'
  u = 10 ** digits
  ys = str(4 * (4 * arcctg(5, u) - arcctg(239, u)))
  c = len(str(maxerr(digits)))
  while ys[-c] == '0':
    c += 1
  return '3.' + ys[1 : -c]

print pi(5)
