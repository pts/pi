import sys
import mpz
a,b,f,g,p,q=0,4,40,24,9,7
# ,(s=$>).sync=s<<'3.'
sys.stdout.write('3.')
while 1:
  a,b,f,g,t=f,g,p*a+q*f,p*b+q*g,a/b
  while f/g==t:
    print t
    a,f=10*(a%b),10*(f%g)
    t=a/b
  p,q=p+q,q+2
