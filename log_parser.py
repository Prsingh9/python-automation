#Parse a log file and count the number of ERROR, WARNING, and INFO lines

import re
from collections import defaultdict

def count_log_levels(filepath) :
	counts = defaultdict(int)
	pattern = re.compile(r'\b(ERROR|WARNING|INFO|DEBUG|CRITICAL)\b')
	
	with open(filepath, 'r') as f :
		for line in f:
			match = pattern.search(line)
			if match:
				counts[match.group(1)] +=1
	return dict(counts)


result = count_log_levels('test.log')
print(result)
