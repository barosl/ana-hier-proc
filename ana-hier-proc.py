#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

val_basis = {
	'품질': {'교/반': 2, '가격': 3},
	'교/반': {'가격': 2},
	'가격': {},
}

val_basis_res = {}

alt_basis = {
	'품질': {
		'백화점': {'재/시': 2},
		'재/시': {},
	},

	'교/반': {
		'백화점': {'재/시': 3},
		'재/시': {},
	},

	'가격': {
		'백화점': {'재/시': 1./2},
		'재/시': {},
	},
}

alt_basis_res = {
	'품질': {},
	'교/반': {},
	'가격': {},
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
