# 4. Increment 10.10.10.1(ip address increment).
# output should be [10.10.10.1,10.10.10.2... 10.10.10.255, 10.10.11.255,10.10.12.255,10.10.13.255.
# 10.10.255.255,10.11.255.255....].

ip = '10.10.10.1'
ip_list = ip.split('.')
result = [ip]
for i in range(3, -1, -1):
	while ip_list[i] != '255':
		ip_list[i] = str(int(ip_list[i]) + 1)
		result.append('.'.join(ip_list))
print(result)