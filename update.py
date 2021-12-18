def main():
	inp = input() 
	lst = []
	while inp:
		lst.append(' - '.join(inp.split(' - ')[0:-1]))
		inp = input()
	for i in lst:
		print('$mm update', i)