#!/usr/local/bin/perl
use integer;
use strict;
require'bigint.pl';
$|=1;
print"3.";
my($k,$a,$b,$f,$g,$p,$q,$d,$e,$l)=(3,0,4,40,24,9,5);
while (1) {
  $l=badd($k,1);
  ($p,$q,$k)=(bmul($k,$k),badd($k,$l),$l);
  ($a,$b,$f,$g)=($f,$g,badd(bmul($p,$a),bmul($q,$f)),badd(bmul($p,$b),bmul($q,$g)));
  while (bdiv($f,$g)eq($d=bdiv($a,$b))) {
    print 0+$d;
    ($a,$f)=(bmul(10,bmod($a,$b)),bmul(10,bmod($f,$g)));
  }
}
