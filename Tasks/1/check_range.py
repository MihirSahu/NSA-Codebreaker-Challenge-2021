import ipaddress

with open('ip_ranges.txt', 'r') as file:
	data = file.readlines()
	data = [line.rstrip() for line in data]

with open('plaintext_address.txt', 'r') as file:
	addr = file.readlines()
	addr = [line.rstrip() for line in addr]

#addr = ['172.24.215.120', '10.31.55.169', '10.61.135.118', '192.168.3.28']

for targetAddress in addr:
	for check in data:
		if ipaddress.ip_address(targetAddress) in ipaddress.ip_network(check):
			print("{yes} is in {yesAgain}".format(yes = targetAddress, yesAgain = check))
