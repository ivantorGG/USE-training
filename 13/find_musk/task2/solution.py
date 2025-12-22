# https://www.youtube.com/watch?v=DBoXMHFFPc4&t=335s

from ipaddress import ip_network

for m in range(33):
    net = ip_network(f'229.117.114.172/{m}', False)
    if '229.117.112.0' in str(net):
        print(m)
        break

# 20
