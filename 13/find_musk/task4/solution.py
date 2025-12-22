# https://www.youtube.com/watch?v=DBoXMHFFPc4&t=525s

from ipaddress import ip_address, ip_network

for m in range(33):
    net = ip_network(f'161.137.200.35/{m}', False)
    if ip_address('161.137.150.118') not in net:
        print(net.netmask)
        break

# 192
