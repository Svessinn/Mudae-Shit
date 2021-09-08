def main():
	inp = input()
	lst = []
	while inp:
		lst.append(inp[0:-20])
		inp = input()
	print(*lst, sep='$')