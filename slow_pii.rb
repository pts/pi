(s=$>).sync=s<<'3.'
a,b,f,g,p,q=0,4,40,24,9,7
while a
a,b,f,g=f,g,p*a+q*f,p*b+q*g
s,a,f=s<<$_,10*(a%b),10*(f%g)while f/g==$_=a/b
p+=q
q+=2
end