#!/usr/local/bin/perl
use integer;
use strict;
require'bigint.pl';
$|=1;
print"3.";
my($a,$b,$f,$g,$p,$q,$d,$e,$l)=(0,4,40,24,9,5);
while ($q=badd($q,2)) {
  ($a,$b,$f,$g)=($f,$g,badd(bmul($p,$a),bmul($q,$f)),badd(bmul($p,$b),bmul($q,$g)));
  ($a,$f)=(bmul(10,bmod($a,$b)),bmul(10,bmod($f,$g)),print$d+0)while($d=bdiv($a,$b))eq bdiv($f,$g);
  $p=badd($p,$q);
}