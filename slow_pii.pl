#!/usr/local/bin/perl
use integer;
use strict;
require'bigint.pl';

# die "".bdiv("+76",+"24");

$|=1;
print"3.";
my($k,$a,$b,$f,$g,$p,$q,$d,$e,$l)=(3, 0, 4, 40, 24);
while (1) {
  # Next approximation
  $l=badd($k,1);
  ($p,$q,$k)=(bmul($k,$k),badd($k,$l),$l);
  ($a,$b,$f,$g)=($f,$g,badd(bmul($p,$a),bmul($q,$f)),badd(bmul($p,$b),bmul($q,$g)));
  # print "$a $b $f $g\n"; sleep 1;
  # Print common digits
  while (1) {
    ($d,$e)=(scalar(bdiv($a,$b)),bdiv($f,$g));
    # die "".bdiv($f,$g);
    # print "de $d $e $f $g\n";
    last if $d ne$e;
    print 0+$d;
    # die;
    ($a,$f)=(bmul(10,bmod($a,$b)),bmul(10,bmod($f,$g)));
  }
}
