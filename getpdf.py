import time
import requests
import socket
def download_pdf(url):
    try:
        print(url)
        start =time.time()
        r = requests.get(url)
        close_time=time.time()
        content=r.content
        size=len(content)
        throughput=size/(close_time-start)
        with open('throughput.txt', 'a+') as f:
            f.write(url + ',' + str(throughput))
            f.write('\n')
    except:
        print("Next")


def split_n():
    data1 = []
    with open('urllist.txt', 'r')as f:
        data = f.readlines()
    for line in data:
        line = line.strip('\n')
        data1.append(line)
    return data1
def get_ip_list(domain):  # 获取域名解析出的IP列表
    ip_list = []
    try:
        addrs = socket.getaddrinfo(domain, None)
        for item in addrs:
           if item[4][0] not in ip_list:
               ip_list.append(item[4][0])
    except Exception as e:
                # print(str(e))
        pass
    return ip_list
def get_domain(ur):
    return ur.split('/')[2]
