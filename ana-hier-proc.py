#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

val_basis = {
	'시/소': {'윤리': 5, '성/확': 1./2, '난이도': 4},
	'윤리': {'성/확': 1./7, '난이도': 1./6},
	'성/확': {'난이도': 4},
	'난이도': {},
}

val_basis_res = {}

alt_basis = {
	'시/소': {
		'무시': {'급한': 3, '전화': 4},
		'급한': {'전화': 2},
		'전화': {},
	},

	'윤리': {
		'무시': {'급한': 1./4, '전화': 1./2},
		'급한': {'전화': 3},
		'전화': {},
	},

	'성/확': {
		'무시': {'급한': 4, '전화': 5},
		'급한': {'전화': 3},
		'전화': {},
	},

	'난이도': {
		'무시': {'급한': 3, '전화': 6},
		'급한': {'전화': 4},
		'전화': {},
	},
}

alt_basis_res = {
	'시/소': {},
	'윤리': {},
	'성/확': {},
	'난이도': {},
}

def normalize_table(basis, basis_res):
	for x in basis:
		for y in basis[x]:
			basis[y][x] = 1./basis[x][y]

		basis[x][x] = 1.

	for x in basis:
		total = sum(row[x] for row in basis.itervalues())
		for row in basis.itervalues():
			row[x] /= total

	for x in basis:
		basis_res[x] = sum(basis[x].itervalues())/len(basis[x])

def print_table(basis, basis_res, fp=sys.stdout):
	for x in basis:
		fp.write('\t%s' % x)
	fp.write('\n')

	for x in basis:
		fp.write('%s\t' % x)
		fp.write('\t'.join('%.3f' % x for x in basis[x].itervalues()))
		fp.write('\t%.3f' % basis_res[x])
		fp.write('\n')

	fp.write('----\n')

normalize_table(val_basis, val_basis_res)
for x in alt_basis: normalize_table(alt_basis[x], alt_basis_res[x])
print_table(val_basis, val_basis_res)
for x in alt_basis: print_table(alt_basis[x], alt_basis_res[x])

for alt in alt_basis.itervalues().next().iterkeys():
	sys.stdout.write('%s:\t' % alt)
	sys.stdout.write('%.3f' % sum(val_basis_res[val] * alt_basis_res[val][alt] for val in alt_basis_res))
	sys.stdout.write('\n')
