#!/usr/local/bin/perl -w
use integer;
use string;


k, a, b, f, g = 2, 4, 1, 12, 4

while TRUE
  # Next approximation
  p, q, k = k*k, 2*k+1, k+1
  a, b, f, g = f, g, p*a+q*f, p*b+q*g
  # Print common digits
  d = a / b
  e = f / g
  while d == e
    print d
    $stdout.flush
    a, f = 10*(a%b), 10*(f%g)
    d, e = a/b, f/g
  end
end
