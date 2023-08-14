import ipaddress

def calculate_network_broadcast(ip, subnet_mask):
    ip_obj = ipaddress.ip_interface(f"{ip}/{subnet_mask}")
    network = ip_obj.network
    broadcast = network.broadcast_address
    return network, broadcast

def calculate_ip_count(subnet_mask):
    ip_count = 2 ** (32 - sum(bin(int(x)).count('1') for x in subnet_mask.split('.')))
    return ip_count - 2

def check_same_network(ip1, ip2, subnet_mask):
    ip1_obj = ipaddress.ip_interface(f"{ip1}/{subnet_mask}")
    ip2_obj = ipaddress.ip_interface(f"{ip2}/{subnet_mask}")
    return ip1_obj.network.network_address == ip2_obj.network.network_address

def find_different_subnet(ip, network, max_subnet_count):
    for prefix_len in range(network.prefixlen + 1, 32):
        subnet = ipaddress.ip_network(ipaddress.ip_interface(f"{ip}/{prefix_len}").network)
        if subnet != network:
            return subnet
    return None

ip1 = input("İlk IP Adresini Girin: ")
ip2 = input("İkinci IP Adresini Girin: ")
subnet_mask = input("Subnet Maskesini Girin: ")

binary_ip1 = '.'.join(format(int(octet), '08b') for octet in ip1.split('.'))
binary_ip2 = '.'.join(format(int(octet), '08b') for octet in ip2.split('.'))
binary_subnet_mask = '.'.join(format(int(octet), '08b') for octet in subnet_mask.split('.'))

network1, _ = calculate_network_broadcast(ip1, subnet_mask)
network2, _ = calculate_network_broadcast(ip2, subnet_mask)

print(f"İlk IP Adresi Binary: {binary_ip1}")
print(f"İkinci IP Adresi Binary: {binary_ip2}")
print(f"Subnet Maskesi Binary: {binary_subnet_mask}")
print(f"Ağ Adresi 1: {network1}")
print(f"Ağ Adresi 2: {network2}")

if check_same_network(ip1, ip2, subnet_mask):
    
    print(f"Bu IP adresleri aynı ağda bulunuyor.")
    c = 1
    max_subnet_count = 5
    subnet = find_different_subnet(ip1, network1, max_subnet_count)
    if subnet:
        print(f"Farklı Network İçin Önerilen Subnet Maskesi: /{subnet.prefixlen}")
    else:
        print("Bu aynı ağda bulunan IP adresleri için farklı networklere root EDILEMEZ.")
else:
    print("Bu IP adresleri birbirine root EDILEBILIR.")
    ip_count = calculate_ip_count(subnet_mask)
    print(f"Verilen Subnet Maskesi ile Alınabilecek Toplam IP Adresi Sayısı: {ip_count} + 2")