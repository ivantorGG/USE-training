# https://www.youtube.com/watch?v=DBoXMHFFPc4&t=600s

from ipaddress import ip_network

c = 0
net = ip_network('172.16.128.0/255.255.192.0', False)

for ip in net:
    ip_bin = f'{int(ip):032b}'
    if ip_bin.count('1') % 2:
        c += 1

print(c)

# 8192
