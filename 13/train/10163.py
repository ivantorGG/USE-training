from ipaddress import ip_address, ip_network

net = ip_network('192.168.156.235/255.255.255.240', False)

print(list(net).index(ip_address('192.168.156.235')))
