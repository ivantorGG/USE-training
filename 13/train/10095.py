from ipaddress import ip_network

net = ip_network('192.168.32.160/255.255.255.240', False)

print(sum(1 for ip in net if not f'{int(ip):032b}'.count('1') % 2))
