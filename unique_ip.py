#Extract all unique IP addresses from an Nginx access log

import re

def extract_unique_ips(filepath) :
	ip_pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
	unique_ips = set()
	with open(filepath, 'r') as f : 
		for line in f :
			match = ip_pattern.match(line)
			if match :
				unique_ips.add(match.group(1))
	return unique_ips

ips = extract_unique_ips('sample_data/access.log')
print(f'unique Ips:{len(ips)}')
print(sorted(ips))
