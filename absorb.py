#!/usr/bin/env python3
assert print, "must be python 3!"
import os
from getpass import getpass as input_pass

def diverge_i(a, b):
	for i in range(min(len(a), len(b))):
		if a[i] != b[i]:
			return i
	return None

orig = input_pass("Copy-paste template password: ")
print("Characters: %d" % len(orig))

score = 0

while score < 20:
	p = input_pass("(%3d) password: " % score)
	if p == orig:
		print("Correct!")
		score += 1
	elif len(p) < len(orig):
		ifail = diverge_i(orig, p)
		if ifail is None:
			print("Wrong! Truncated. Next three letters are '%s'" % orig[len(p):len(p)+3])
			score -= 1
		else:
			ifail = max(ifail, 1)
			print("Wrong! Too short, and you wrote '%s' instead of '%s'" % (p[ifail-1:ifail+2], orig[ifail-1:ifail+2]))
			score -= 1
	elif len(p) > len(orig):
		print("Wrong! (too long)")
		score -= 1
	else:
		ifail = max(diverge_i(orig, p), 1)
		print("Wrong! You wrote '%s' instead of '%s'" % (p[ifail-1:ifail+2], orig[ifail-1:ifail+2]))
		score -= 1
	if score < 0:
		score = 0

os.system("clear") # don't display hints anymore
print("Reached score of 20!")
