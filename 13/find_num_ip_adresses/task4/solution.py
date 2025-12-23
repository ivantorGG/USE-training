# https://www.youtube.com/watch?v=DBoXMHFFPc4&t=1095s
# This one is a bit tricky, basic iterating loop in loop will take too long.
# The more '1' in a subnet mask, the less addresses in the subnet.

from ipaddress import ip_address, ip_network


for m in range(32, -1, -1):
    net = ip_network(f'193.45.192.104/{m}', strict=False)
    if ip_address('193.45.206.210') in net:
        print(sum(1 for ip in net if not f'{int(ip):b}'.count('1') % 2))
        break

# 2048
