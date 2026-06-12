# Find all lines containing a specific HTTP status code (e.g., 500) in logs

import re 
from collections import Counter

def find_status_code_lines (filepath, status_code) :
	pattern = re.compile(r' "\S+ \S+ \S+" ' + status_code + r' ')
	results = []
	
	with open(filepath, 'r') as f :
		for line in f:
			if pattern.search(line) :
				results.append(line.strip())

	print(f'Found {len(results)} lines with status code {status_code}')
	return results

find_status_code_lines('sample_data/access.log', '500')
