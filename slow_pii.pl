require'bigint.pl';$|=1;print"3.";($a,$b,$f,$g,$p,$q)=(0,4,40,24,9,5);while($q
=badd($q,2)){($a,$b,$f,$g)=($f,$g,badd(bmul($p,$a),bmul($q,$f)),badd(bmul($p,$
b),bmul($q,$g)));($a,$f)=(bmul(10,bmod($a,$b)),bmul(10,bmod($f,$g)),print$_+0)
while($_=bdiv($a,$b))eq bdiv($f,$g);$p=badd($p,$q)}