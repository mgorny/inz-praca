#!/usr/bin/env python

import h2o

p = 10
T1 = 333.15
T2 = 773.15

T = T1
while T <= T2:
	print '%f %f' % (h2o.H2O(p, T).s, T)
	T += 1
