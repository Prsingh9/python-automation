import re
from collections import defaultdict

def count_log_levels(filepath) :
	counts = defaultdict(int)
	pattern = re.compile(r'\b(ERROR|WARNING|INFO|DEBUG|CRITICAL)\b')
	timestamp_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
	
	first_error = None
	last_error = None

	with open(filepath,'r') as f : 
		for line in f :
			match = pattern.search(line)
			if match :
				counts[match.group(1)] += 1
		
			if match.group(1) == "ERROR" :
				ts_match = timestamp_pattern.search(line)
				if ts_match :
					ts = ts_match.group(0)
				if first_error == None :
					first_error = ts
				last_error = ts

	print(f"first ERROR: {first_error}")
	print(f"last ERROR: {last_error}")
	return dict(counts)

result = count_log_levels('test.log')
print(result)
