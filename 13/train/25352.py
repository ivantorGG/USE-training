from ipaddress import ip_network

net = ip_network('190.202.83.62/255.255.252.0', 0)

print(sum(map(int, str(net[-2]).split('.'))))  # Except broadcasting
