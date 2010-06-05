#! /usr/bin/python2.4

import sys
import time

def arcctg(x, u):
  sum = xpower = u // x
  n = 3
  sign = -1
  term = 1
  while term:
    xpower = xpower // (x*x)
    term = xpower // n
    sum += sign * term
    sign *= -1
    n += 2
  return sum

def pi(digits):
  u = 10**(digits + 10)
  pi = 4 * (4*arcctg(5, u) - arcctg(239, u))
  return pi // 10**10

print pi(100000)

#for i in range(1000):
#  sys.stdout.write(str(pi(i) % 10))
#  sys.stdout.flush()
#  time.sleep(0.01)
