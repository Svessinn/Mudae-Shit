def main():
	inp = input()
	lst = []
	while inp:
		lst.append(inp.split(' - ')[1].split(' · ')[0])
		inp = input()

	inp = input()
	while inp:
		if inp in lst:
			lst.remove(inp)
		inp = input()
	print(*lst, sep='$')