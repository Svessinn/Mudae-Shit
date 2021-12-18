import json
def main():
	with open("Bundle/bundles.txt", "r", encoding="UTF-8") as f:
		with open("Bundle/newBundles.json", encoding="UTF-8") as fi:
			data = json.load(fi)
		bundles = [line.strip() for line in f]
		for bundle in data:
			if bundle["Bundle"] in bundles:
				bundles.remove(bundle["Bundle"])
	with open("Bundle/bundles.txt", "a", encoding="UTF-8") as f:
		f.seek(0)
		f.truncate()
		for i in bundles:
			print(i, file=f)