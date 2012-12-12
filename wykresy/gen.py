#!/usr/bin/env python

import h2o

# krzywa nasycenia
Tmin = 273.15
T = Tmin
while True:
	try:
		z = h2o.H2O(x=0, T=T)
	except ValueError:
		break

	print '%f %f' % (z.s, z.T)
	if T >= 645.15:
		T += .2
	else:
		T += 1

# pkryt
z = h2o.H2O(x=0, T=647.096)
print '%f %f' % (z.s, z.T)

while T > Tmin:
	if T > 645.15:
		T -= .2
	else:
		T -= 1
	z = h2o.H2O(x=1, T=T)

	print '%f %f' % (z.s, z.T)

