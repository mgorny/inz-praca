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

def Isobar(p, s1, s2):
	s = s1
	step = (s2 - s1) / 100
	while s <= s2:
		yield h2o.H2O(p=p, s=s)
		s += step

def SatCurve():
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

def Boiler(st, T2):
	p = st.p
	T = st.T

	while T <= T2:
		yield h2o.H2O(p, T)
		T += 1

def Turbine(st, p2, eff = 1):
	p = st.p

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

def Pump(st, p2, etai = 1):
	eff = 1/etai

	p = st.p
	while p < p2:
		yield st.expand(p, eff)

		if p < 1:
			p += 1
		elif p <= .09:
			p += .6
		elif p < .009:
			p += .06
		else:
			p += .006

def Condenser(st):
	yield st
	yield h2o.H2O(p=st.p, x=0)

def wr(f, c):
	with Tab(f) as t:
		for x in c:
			t.write(x)
			l = x

	return l

with open('.stamp', 'w'):
	pass

wr('_nasyc.txt', SatCurve())
s1 = h2o.H2O(10, 773.15)
wr('turbina-i.txt', Turbine(s1, .006))
s2 = wr('turbina.txt', Turbine(s1, .006, .8))
s3 = wr('skraplacz.txt', Condenser(s2))
wr('pompa-i.txt', Pump(s3, s1.p))
s0 = wr('pompa.txt', Pump(s3, s1.p, .8))
wr('kociol.txt', Boiler(s0, s1.T))

wr('izobara-10.txt', Isobar(s1.p, .5, .55))

assert(s2.T <= s0.T)
