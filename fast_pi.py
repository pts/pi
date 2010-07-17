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

def pi0(digits0):
  u = 10 * digits0
  return 4 * (4*arcctg(5, u) - arcctg(239, u))

def maxerr(digits0):
  return (286135312 * digits0 + 31739381 + 9999999) // 10000000

def pi(digits0):
  m0 = maxerr(digits0)
  lm0 = len(str(m0))
  digits = lm0 + digits0
  m = maxerr(digits)
  lm = len(str(m))
  if lm > lm0:
    digits += 1
    assert lm == lm0 + 1
  u = 10 ** digits
  return (4 * (4 * arcctg(5, u) - arcctg(239, u))) // (10 ** lm)

def pigood(digits):
  if digits <= 1:
    return '3'
  ys = str(pi(digits))
  c = 1
  while ys[-c] == '0':
    c += 1
  return '3.' + ys[1 : -c]

assert pigood(77) == ('3.141592653589793238462643383279502884197169399' +
                      '375105820974944592307816406286')

if __name__ == '__main__':
  digits = 8
  xs = pigood(digits)
  sys.stdout.write(xs)
  sys.stdout.flush()
  while True:
    digits <<= 1
    ys = pigood(digits)
    assert ys.startswith(xs)
    sys.stdout.write(ys[len(xs):])
    sys.stdout.flush()
    xs = ys
