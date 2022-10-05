import socks
import socket
import requests
import json

#only to check ip address
def ip_data():
    ip_from_ican = requests.get('https://httpbin.org/ip').text
    j_data = json.loads(ip_from_ican)
    return j_data["origin"]

#will decorate the function to run over tor
def use_proxy(func):

    port_no = 9150

    def wrapper_func():
        #check before proxy ip
        before_ip = ip_data()
        after_ip = before_ip
        try:
            #Setup Proxy Before Function
            socks.set_default_proxy(socks.SOCKS5,"localhost",port_no)
            socket.socket = socks.socksocket

            #check after proxy ip
            after_ip = ip_data()
        except:
            print('[-] TOR ISN\'T CONNECTED ....')

        if before_ip != after_ip:
            print('[+] Connected To TOR ....\n')
            func()
        else:
            print('[-] TOR CONNECTION FAILED !!!!! ....')
    return wrapper_func

@use_proxy
def run_with_proxy():
    print(ip_data())

run_with_proxy()
