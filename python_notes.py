# # From Roger's class 2 lecture

# # def my_function(my_list = [5, 4, 3, 2, 1]):
# #    for number in my_list:
# #        print(number)
#     # pass

# # import datetime
# # now = datetime.datetime.now()
# # print(now)

# # new_date = datetime.date(1999, 12, 31)
# # print(new_date)

# # import time

# # time_now = time.localtime() # tiime.time()
# # print(time_now)

# # time.sleep(5)
# # print('Did I sleep for 5 seconds')

# # import os
# # result = os.system('ping localhost -c 4')


# # if __name__ == "__main__":
# #    my_variable = [1, 2, 3, 4, 5]
# #    my_function(my_variable)
# #    my_function()

# # From Roger's class 6 lecture

# # Declare functions
# def encrypt(number, key):
#     encrypted_text = ""

#     for num in number:
#         numb = int(num, 16)
#         shifted_num = (numb + key) % 10
#         encrypted_text += str(shifted_num)
#     return encrypted_text

# def decrypt(encoded, key):
#     return encrypt(encoded, -key)

# if __name__ == "__main__":
#     encrypted = encrypt('123456', 3)
#     print(encrypted)
#     decrypted = decrypt(encrypted, 3)
#     print(decrypted)

# # must pip install cryptography package library then import Fernet module from it
# from cryptography.fernet import Fernet

# # generate key
# key = Fernet.generate_key()

# # assign key value to var
# f = Fernet(key)

# # convert PT to CT, 
# token = f.encrypt(b"encryption is fun")

# # 'b' = byte format, in this case binary...this can be removed using decode() method while printing original message (in libary's internal method)

# #  display CT
# print(token)

# # decrypt CT
# d = f.decrypt(token)

# # display PT
# print(d)

# # generate key and save to file
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#     return key

# # loads key from current directory named 'key.key'
# def load_key():
#     return open("key.key", "rb").read()

# # generate and write a new key
# write_key()

# # load previously generated key
# key = load_key()
# print("Key is " + str(key.decode('utf-8')))

# message = "hello friend".encode()
# print("PT is " + str(message.decode('utf-8')))

# # initialize Fernet class
# f = Fernet(key)

# # encrypt the message
# encrypted = f.encrypt(message)

# # print how it looks
# print("CT is " + encrypted.decode('utf-8'))

# # Roger's class 7 warmup & lecture

# import os

# # '.' tells python to run walk specifically from current directory
# import os
# for root, dirs, files in os.walk("."):
#     print(root)
#     print(dirs)
#     print(files)
#     # 
#     print('-' * 88)
# for root, dirs, files in os.walk("/home/david"):
#     print(root)
#     print(dirs)
#     print(files)
#     print('-' * 88)
# for root, dirs, files in os.walk("/home/david"):
#     print(root)
#     print(dirs)
#     print(files)
#     for file in files:
#         with open(file) as f:
#             print(f.read())
#     print('-' * 88)

# # Roger's lecture class 11

# # have to install scapy w/ 'pip3 install scapy' and only import modules you'll NEED to work
# # from scapy.all import Ether, IP, sniff, ARP, sr1, ICMP, TCP

# # test_frame = Ether() / IP()

# # # print(test_frame)
# # print('-' * 80)
# # print(test_frame.show())
# # print('-' * 80)
# # # good to run '.summary' after '.show'
# # # print(test_frame.summary())
# # print('-' * 80)

# # # need escalated privileges for certain functions/tasks, enter 'sudo' before running code
# # # packets = sniff(count=10)
# # # for _ in packets:
# # #     num = 0
# # #     # this will show detailed info on packets needed for ops challenge
# # #     print(packets[num].show())
# # #     num += 1

# # # ARP resolves IP address to MAC addresses
# # request = ARP()
# # print(request)

# # request2 = sr1(IP(dst='scanme.nmap.org')/ICMP())
# # if request2:
# #     print(request2.show())

# # host = 'scanme.nmap.org'
# # port_range = 22
# # src_port = 22
# # dst_port = 22

# # response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags='5'), timeout=1, verbose=0)
# # print(response.show())

# Roger's class 12 Lecture

# ipaddress module is VERY USEFUL!
import ipaddress
from scapy.all import ICMP, IP, sr1, TCP

ip = ipaddress.ip_address('127.0.0.1')
print(f'{ip}: is loopback: {ip.is_loopback}')

ip2 = ipaddress.ip_address('10.0.2.2')
print(f'{ip2}')

network = "10.0.2.0/24"
ip_list = ipaddress.IPv4Network(network).hosts()
hosts_count = 0

# can't 'Ctrl+C' without doing it the # of times there are hosts
for host in ip_list:
    print("Pinging", str(host), "- please wait...")
    response = sr1(
        IP(dst=str(host))/ICMP(),
        timeout=2,
        verbose=0
    )
# make sure not to ping broadcast or host IP

# notes from demo/warmup time class 16

# import mods
import nltk
import ssl
from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    nltk.download('words')
    word_list = words.words()
    # print(word_list)
    return word_list

def check_words(words):
    user_input = input("Please enter a word: ")
    if user_input in words:
        print("That word is indeed in the dictionary!")
    else:
        print("That word isn't in the dictionary.")

def load_file():
    password_list = []
    with open('rockyou.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            password_list.append(line)
            print(password_list)

if __name__ == "__main__":
    ext_words = get_words()
    # print(ext_words)
    # check_words(ext_words)
    load_file()