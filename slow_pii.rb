def testt()
  p "test"
  1
end


def alma()
  p "get_alma"
  false
end

def alma=(n)
  p "alma="
end

#self.alma=5
self.alma||=5

exit

STDOUT.sync=!print("3.")
k,a,b,f,g = 3,0,4,40,24

while TRUE
  p,q,k = k*k,2*k+1,k+1
  a,b,f,g = f,g,p*a+q*f,p*b+q*g
  d = a / b
  e = f / g
  while d == e
    print d
    $stdout.flush
    a,f = 10*(a%b),10*(f%g)
    d,e = a/b,f/g
  end
end
