(s=$>).sync=s<<'3.'
k,a,b,f,g=3,0,4,40,24
while a
p,q,k=k*k,2*k+1,k+1
a,b,f,g=f,g,p*a+q*f,p*b+q*g
a,f,s=10*(a%b),10*(f%g),s<<p while f/g==p=a/b
end