from getpdf import get_domain, split_n
import socket
data=split_n()
domain=[]
iplist=[]
for i in data:
    d=get_domain(i)
    domain.append(d)
print(len(domain))
for d in domain[8370:9343]:
    try:
        my=socket.gethostbyname(d)
        # print(my)
        iplist.append(my)
    except:
        print(0)
        iplist.append(0)
with open('iplist.txt','a+') as f:
    for item in iplist:
        f.write('%s\n' % item)
# for u in domain:
#     my=socket.gethostbyname(u)
#     print(my)
#     iplist.append(u)
