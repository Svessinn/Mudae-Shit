def main():
	inp = input()
	lst = []
	while inp:
		lst.append(inp.split(' (')[0])
		inp = input()
	print(*lst, sep='$')

