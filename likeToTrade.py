from collections import defaultdict as ddict
def main():
	inp =  input()
	dct = ddict(list)
	while inp:
		i = list(inp.split('  :revolving_hearts: => '))
		dct[i[1]].append(i[0])
		inp = input()
	lst = []
	for i in dct:
		lst.append([i, dct[i]])
	for i in range(len(lst)):
		lst[i][1] = sorted(lst[i][1])
	lst.sort(key=lambda x:x[0].capitalize())

	for i in lst:
		print(i[0] + ': ', end='')
		print(*i[1], sep=', ', end='\n\n')
