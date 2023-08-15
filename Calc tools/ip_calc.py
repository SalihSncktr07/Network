import ipaddress

def calculate_network_broadcast(ip, subnet_mask):
    ip_obj = ipaddress.ip_interface(f"{ip}/{subnet_mask}")
    network = ip_obj.network
    broadcast = network.broadcast_address
    return network, broadcast

ip_address = "192.168.3.0"
subnet_mask = "255.255.252.0"

network, broadcast = calculate_network_broadcast(ip_address, subnet_mask)
print(f"IP Adresinin Ağı(Network): {network}")
print(f"IP Adresinin Yayın Adresi(Broadcast): {broadcast}")

while True:
    pass