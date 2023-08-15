import ipaddress

def calculate_network_broadcast(ip, subnet_mask):
    ip_obj = ipaddress.ip_interface(f"{ip}/{subnet_mask}")
    network = ip_obj.network
    broadcast = network.broadcast_address
    return network, broadcast

def calculate_ip_count(subnet_mask):
    ip_count = 2 ** (32 - sum(bin(int(x)).count('1') for x in subnet_mask.split('.')))
    return ip_count - 2

ip_address = "192.168.0.0"
subnet_mask = "255.255.255.0"

binary_ip = '.'.join(format(int(octet), '08b') for octet in ip_address.split('.'))
binary_subnet_mask = '.'.join(format(int(octet), '08b') for octet in subnet_mask.split('.'))

network, broadcast = calculate_network_broadcast(ip_address, subnet_mask)
ip_count = calculate_ip_count(subnet_mask)

print(f"IP Adresi Binary: {binary_ip}")
print(f"Subnet Maskesi Binary: {binary_subnet_mask}")
print(f"Ağ Adresi: {network}")
print(f"Yayın Adresi: {broadcast}")
print(f"Verilen IP Adresi ve Alt Ağ Maskesi ile Alınabilecek Toplam Üye IP Adresi Sayısı: {ip_count} + 2")