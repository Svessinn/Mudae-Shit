def main():
	inp = input() # Input your $mmyd list 
	ls = []
	while inp:
		if 'Soulkeys' in inp:
			lst = [ inp.split(' · ')[0], int(inp.split(' · ')[1].split(' (')[1].split(') ')[0][:-1]), int(inp.split(' · ')[1].split('s: ')[1][:-1]) ]
			ls.append([ lst[0], lst[1]-lst[2] ])
		else:
			ls.append([ inp.split(' · ')[0], int(inp.split(': (')[1][:-1]) ])
		inp = input()
	for i in ls:
		if i[1]:
			print('$rk', i[0], '$', i[1])
