#!/usr/bin/env python3
import scapy.all as scapy
import optparse

print('############################################################################################################################################')
print('')
print('  ########     ##       ##       ##    ##   ########  ')
print('  ##           ##        ##     ##     ##      ##     ')
print('  ##           ##         ##   ##      ##      ##   ')
print('  ########     ##           ####       ##      ## ')
print('  ##           ##         ##    ##     ##      ##  ')
print('  ##           ##        ##      ##    ##      ##      ')
print('  ##           ##       ##        ##   ##      ##     ')
print('')
print('############################################################################################################################################')
print('')
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-r', "--range", dest="target", help="Target IP / IP range")
    (options, argument) = parser.parse_args()
    if not options.target:
        parser.error("please enter an ip range")
    return options
    
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # we create a object that represent an ARP packet and set the pdst to ip
    print(arp_request.summary()) # prints the summary of what the script does
    # scapy.ls(scapy.ARP()) # it the shows the list of variables we can set for a class
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # creates an ethernet object and set the destination mac as the broadcast mac
    arp_request_broadcast = broadcast/arp_request # we combine both packets into 1
    # arp_request_broadcast.show() # shows more info on each packet
    # to send packets and recieve packets split into two parts the answered and unanswered and make it less verbose
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    client_list=[]
    # print(answered_list.summary()) prints the summary of the sent packets
    for element in answered_list: # iterates through the answered list
        client_dict = {"ip": element[1].psrc, "MAC": element[1].hwsrc}
        client_list.append (client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc) # to print the source ip address and source MAC address of the packet
    return client_list
    
def print_result(result_list):
    print ("IP\t\t\tMAC ADDRESS\n -------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["MAC"])
options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
