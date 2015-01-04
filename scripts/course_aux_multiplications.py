# -*- coding: utf-8 -*-
"""
Couse aux multiplications (aka multiplication racing)
=====================================================

The goal is to answer to the multiplications into a minimum amount of time.
To start, enter RETURN, then answer multiplications. 
Each time there is a bad answer, the same multiplication will be prompted again
At the end, the time taken to answer the NB multiplications is displayed
The game is restarted all the time : Control-C to stop playing.
The game will ask NB multiplications with numbers between MIN and MAX

The idea is to do it yourself, get your time,
then ask your kid to do it until his time is less than yours +50% or +100%

Note : you can change variables a the beginning to match your language 
       and what table your kid is learning
"""

from random import randint
from datetime import datetime

MIN = 2
MAX = 9
NB = 20

GO_MSG = 'GO !'
READY_MSG = 'Prêt ?'
NO_MSG = 'NON !!'
TIME_MSG = 'Temps'

while True:
	print '\n\n'
	raw_input(READY_MSG)
	print '%s \n\n' % GO_MSG

	n = 1
	t1 = datetime.now()

	while True:
		a = randint(MIN,9)
		b = randint(MIN,MAX)
		t = a * b
		while True:
			try:
				r = int(raw_input('%d) %d x %d = ' % (n,a,b)))
			except ValueError:
				pass
			if r == t:
				break
			else:
				print "\n\n %s \n\n" % NO_MSG
		
		n += 1
		if n > NB:
			break
	t2 = datetime.now()
        dt = t2-t1
	print "\n\n%s : %d.%d s \n\n" % (TIME_MSG,dt.seconds,dt.microseconds/100000) 
