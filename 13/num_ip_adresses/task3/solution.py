# https://www.youtube.com/watch?v=DBoXMHFFPc4&t=865s

from ipaddress import ip_network

c = 0
net = ip_network('94.253.128.0/255.255.128.0', False)

for ip in net:
    ip_bin = f'{int(ip):032b}'
    if ip_bin.count('1') % 6 and ip_bin.endswith('101'):
        c += 1

print(c)

# 3656
