# https://www.youtube.com/watch?v=DBoXMHFFPc4&t=420s

from ipaddress import ip_address, ip_network

for m in range(32, -1, -1):
    net = ip_network(f'215.171.155.54/{m}', False)
    if ip_address('215.171.145.37') in net:
        print(net.netmask)
        break

# 240
