import sys
w=sys.stdout.write
a,b,f,g,p,q=0,4,40L,24,9,7L
w('3.')
while 1:
 a,b,f,g=f,g,p*a+q*f,p*b+q*g
 t=a/b
 while f/g==t:w(repr(t)[-2]);sys.stdout.flush();a,f=10*(a%b),10*(f%g);t=a/b
 p,q=p+q,q+2