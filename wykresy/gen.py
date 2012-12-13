#!/usr/bin/env python

from __future__ import with_statement
import h2o

class Tab(object):
	def __init__(self, path):
		self._f = open(path, 'w')
		self._f.write('p T h s\n')

	def write(self, p):
		self._f.write('%f %f %f %f\n' % (p.p, p.T, p.h, p.s))

	def __enter__(self):
		return self

	def __exit__(self, *exc):
		self._f.close()
		return False

class SatCurve(object):
	def __iter__(self):
		Tmin = 273.15
		Tkr = 647.096

		T = Tmin
		while T < Tkr:
			yield h2o.H2O(x=0, T=T)

			if T >= 645.15:
				T += .2
			else:
				T += 1

		# punkt krytyczny
		yield h2o.H2O(x=0, T=Tkr)

		while T > Tmin:
			if T > 645.15:
				T -= .2
			else:
				T -= 1

			yield h2o.H2O(x=1, T=T)

class Boiler(object):
	def __init__(self, st, T2):
		self.st = st
		self.T2 = T2

	def __iter__(self):
		p = self.st.p
		T = self.st.T
		T2 = self.T2

		while T <= T2:
			yield h2o.H2O(p, T)
			T += 1

class Turbine(object):
	def __init__(self, st, p2, etai = 1):
		self.st = st
		self.p2 = p2
		self.etai = etai

	def __iter__(self):
		st = self.st

		p = st.p
		p2 = self.p2
		eff = self.etai
		while p >= p2:
			yield st.expand(p, eff)

			if p > 1:
				p -= 1
			elif p > .11:
				p -= .1
			elif p >= .011:
				p -= .01
			else:
				p -= .001

class Condenser(object):
	def __init__(self, st):
		self.st = st

	def __iter__(self):
		yield self.st
		yield h2o.H2O(p=self.st.p, x=0)

def wr(f, c):
	with Tab(f) as t:
		for x in c:
			t.write(x)
			l = x

	return l

with open('.stamp', 'w'):
	pass

wr('_nasyc.txt', SatCurve())
s0 = h2o.H2O(10, 333.15)
s1 = wr('kociol.txt', Boiler(s0, 773.15))
wr('turbina-i.txt', Turbine(s1, .006))
s2 = wr('turbina.txt', Turbine(s1, .006, .8))
wr('skraplacz.txt', Condenser(s2))

assert(s2.T <= s0.T)
