def main():
	inp = input()
	lst = []
	ls = []
	l = []
	while inp:
		if inp != 'Zero Two':
			lst.append('$ai '+inp+'$https://i.imgur.com/fqbFdYD.png')
			ls.append('$im '+inp)
			l.append('$c '+inp+'$')
		inp = input()
	print(*lst, sep='\n')
	print()
	print(*ls, sep='\n')
	print()
	print(*l, sep='\n')
