def main():
	inp = input()
	lst = set()
	while inp:
		i = inp.split()[1:-1]
		if 'Op' in i or 'op' in i:
			i = i[0:-2]
		if 'S1' in i or 'S2' in i or 'S3' in i or 'S4' in i:
			i = i[0:-1]
		i = ' '.join(i)
		lst.add(i)
		inp = input()
	lst = list(lst)
	lst.sort(key=lambda x:x.capitalize())
	print(*lst, sep='\n')
		