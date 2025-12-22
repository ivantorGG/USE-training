from ipaddress import ip_address, ip_network

for mask in range(32, -1, -1):
    net = ip_network(f'211.115.61.154/{mask}', False)
    if ip_address('211.115.59.137') in net:
        print(net.netmask)
        break
