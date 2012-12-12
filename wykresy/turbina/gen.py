#!/usr/bin/env python

from __future__ import with_statement

import h2o

def write(f, eff):
	T1 = 773.15
	p1 = 10
	p2 = .003

	st = h2o.H2O(p1, T1)
	p = p1
	while p >= p2:
		z = st.expand(p, eff)
		f.write('%f %f\n' % (z.s, z.T))
		if p > 1:
			p -= 1
		elif p > .11:
			p -= .1
		elif p >= .011:
			p -= .01
		else:
			p -= .001

with open('Ts.txt', 'w') as f:
	write(f, 1.0)

with open('Ts2.txt', 'w') as f:
	write(f, 0.8)
