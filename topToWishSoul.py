def main():
	lst = []
	inp = input()
	while inp:
		i = inp.split(' - ')
		if '(Soulkeys:' in i[2]:
			i2 = int(i[2][:-1].split(': ')[-1])
			if i2 < 10:
				lst.append(i[1].split(' :revolving_hearts:')[0])
		else:
			lst.append(i[1].split(' :revolving_hearts:')[0])
		inp = input()
	print(*lst, sep='$')
