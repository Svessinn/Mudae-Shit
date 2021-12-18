def main():
	inp = input() 
	lst = []
	while inp:
		lst.append(list(inp.split(' - ')))
		inp = input()
	for i in range(len(lst)):
		lst[i][0] = int(lst[i][0][1::])
	lst.sort(key=lambda x:x[0])
	for i in range(len(lst)):
		lst[i] = lst[i][1]
	inp = input()
	while inp:
		if inp in lst:
			lst.remove(inp)
		inp = input()
	print(*lst, sep='$')
