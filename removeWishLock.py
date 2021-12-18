def main():
	inp = input()
	lst = []
	while inp:
		lst.append(inp.split(' :white_')[0])
		inp = input()
	print(*lst, sep='$')