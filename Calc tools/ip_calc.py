import ipaddress

def calculate_network_broadcast(ip, subnet_mask):
    ip_obj = ipaddress.ip_interface(f"{ip}/{subnet_mask}")
    network = ip_obj.network
    broadcast = network.broadcast_address
    return network, broadcast

ip_address = input("IP Adresini giriniz: ")
subnet_mask = input("Subnet Mask giriniz: ")

network, broadcast = calculate_network_broadcast(ip_address, subnet_mask)
print(f"IP Adresinin Ağı(Network): {network}")
print(f"IP Adresinin Yayın Adresi(Broadcast): {broadcast}")

while True:
    input("")
    break