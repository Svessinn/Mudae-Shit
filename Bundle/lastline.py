def main():
	inp = input()
	out = '' + inp+'\n'
	last = ' $wa, '
	while inp != 'stop':
		if ' $wa, ' not in last:
			out+=inp+'\n'
		last = inp
		inp = input()
	with open("Bundle/output.json", "a") as outfile:
		# Clearing the data from the output file
		outfile.seek(0)
		outfile.truncate()
		# Dumping the output data to the output file
		print(out, file=outfile)
