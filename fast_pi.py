#! /usr/bin/python2.4
# -*- coding: utf-8 -*-

import sys

def arcctg(x, u):
  #assert x in (5, 239)
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

# sum a (fölső) cikluson belül i-szer módosul
# (i + 1)-szer lépünk bele a ciklusba
# a kerekítési hiba abszolút értéke abkh <= 2 * i + 1 == 2 * (i + 1) - 1
# u/5/3/25**(i+1) < 1  (a ciklusvég-feltétel: not term)
# u/5/3/25**(i) >= 1  (még épp nem ért véget a ciklus)
#
# u / 15 >= 25 ** i
# log_25(u / 15) >= i
# 2 * log_25(u / 15) >= 2 * i
# 2 * log_25(u / 15) + 1 >= 2 * i + 1
# 2 * log_25(u / 15) + log_25(25) >= 2 * i + 1
# 2 * log_25(u * 25 / 15) >= 2 * i + 1
# 2 * log_10(u * 25 / 15) / log_10(25) >= 2 * i + 1
# 2 * log_10(u) / log_10(25) + log_10(25 / 15) / log_10(25) >= 2 * i + 1
# 1.43067656 * log_10(u) + 0.15869691 >= 2 * i + 1 >= abkh
# 1.43067656 * log_10(u) + 0.15869691 >= abkh

def pi0(digits0):
  u = 10 * digits0
  return 4 * (4*arcctg(5, u) - arcctg(239, u))

# a pi0(digits0) (+ 10 nélküli) kerekítési hibája legfeljebb abkhpi0
# digits0 == log_10(u)
# 20 * (1.43067656 * log_10(u) + 0.15869691) >= abkh * 20 >= abkhpi0
# 28.6135312 * digits0 + 3.17393806 >= abkhpi0

def maxerr(digits0):
  return (286135312 * digits0 + 31739381 + 9999999) // 10000000

def pi(digits0):
  """The (x + 1) digits might be wrong, where x is the number of zeroes at the
  end of the returned value."""
  m0 = maxerr(digits0)   # 100  -> 2865
  lm0 = len(str(m0))     # 2865 -> 4
  digits = lm0 + digits0 # 100 + 5
  m = maxerr(digits)
  lm = len(str(m))
  if lm > lm0:
    digits += 1
    assert lm == lm0 + 1

  u = 10 ** digits
  return (4 * (4 * arcctg(5, u) - arcctg(239, u))) // (10 ** lm)

def pigood(digits):
  """Calculate pi up to the first `digits' digits.

  All returned digits are correct.

  May return a string with less than `digits' digits.
  """
  if digits <= 1:
    return '3'
  ys = str(pi(digits))
  c = 1
  while ys[-c] == '0':
    c += 1
  return '3.' + ys[1 : -c]

print len(str(maxerr(350000000)))

assert str(pi(77)) == '314159265358979323846264338327950288419716939937510582097494459230781640628620'
assert str(pigood(77)) == '3.141592653589793238462643383279502884197169399375105820974944592307816406286'

# Sanity-check that our maxerr calculation is right.
if True:
  xs = pigood(100)  # DEBUG: 1000
  for digits in xrange(2, len(xs) - 1):
    ys = pigood(digits)
    assert xs.startswith(ys), '%s\n%s\n%s\n' % (digits, xs, ys)


digits = 8
xs = pigood(digits)
sys.stdout.write(xs)
sys.stdout.flush()
written = len(xs)
while True:
  digits <<= 1  # Double the number of digits.
  ys = pigood(digits)
  assert ys.startswith(xs)
  sys.stdout.write(ys[written:])
  sys.stdout.flush()
  xs = ys
