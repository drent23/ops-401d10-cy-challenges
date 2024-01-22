from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP

test_frame = Ether() / IP()

# print(test_frame)
print('-' * 80)
print(test_frame.show())
print('-' * 80)
# good to run '.summary' after '.show'
# print(test_frame.summary())
print('-' * 80)

# need escalated privileges for certain functions/tasks, enter 'sudo' before running code
# packets = sniff(count=10)
# for _ in packets:
#     num = 0
#     # this will show detailed info on packets needed for ops challenge
#     print(packets[num].show())
#     num += 1

# ARP resolves IP address to MAC addresses
request = ARP()
print(request)

request2 = sr1(IP(dst='scanme.nmap.org')/ICMP())
if request2:
    print(request2.show())

host = 'scanme.nmap.org'
port_range = 22
src_port = 22
dst_port = 22

response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='5'), timeout=1, verbose=0)
print(response.show())