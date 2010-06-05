#! /usr/bin/python2.4

import sys

k, a, b, a1, b1 = 2, 4, 1, 12, 4

while True:
  # Next approximation
  p, q, k = k*k, 2*k+1, k+1
  a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
  # Print common digits
  d = a / b
  d1 = a1 / b1
  while d == d1:
    sys.stdout.write(str(d))
    sys.stdout.flush()
    a, a1 = 10*(a%b), 10*(a1%b1)
    d, d1 = a/b, a1/b1
