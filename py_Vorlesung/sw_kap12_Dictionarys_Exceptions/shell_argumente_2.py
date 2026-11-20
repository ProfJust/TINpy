# shell_argumente.py
# usage: Aufruf mit Argumneten aus dem Terminal
# ys/shell_argumente_2.py 5 2

from sys import argv


try:
	n=int(argv[1])
except IndexError:
	print('Fehlender Aufrufparameter')
except ValueError:
	print('Integer erwartet')

else:
	if n>=0:
		print('%d hoch 2 = %d' % (n, n*n))
	else:
		print('Argument muss sein >0')

