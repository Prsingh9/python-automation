import re
from collections import defaultdict

def error_per_min(filepath) :
	pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}):\d{2}.*ERROR')
	counts = defaultdict(int)

	with open(filepath,'r') as f :
		for line in f :
			match = pattern.search(line)
			if match :
				minute_key = match.group(1)
				counts[minute_key] +=1

	for minute in sorted(counts) :
		print(f'{minute} -> {counts[minute]} errors')
	return dict(counts)

error_pmin = error_per_min('sample_data/test.log')
print(error_pmin)

