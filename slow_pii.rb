a,b,f,g,p,q,t=0,4,?(,24,9,5,(s=$>).sync=s<<'3.'
while q+=2
a,b,f,g=f,g,p*a+q*f,p*b+q*g
s,a,f=s<<t,10*(a%b),10*(f%g)while f/g==t=a/b
p+=q
end