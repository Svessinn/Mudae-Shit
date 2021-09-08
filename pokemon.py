def main():
	inp = input()
	lst = []
	while inp:
		lst.append(inp.split(':')[2].strip())
		inp = input()
	inp = input()
	while inp:
		i = inp.split(':')[2].strip()
		lst.remove(i)
		inp = input()
	print(*lst, sep=', ')
