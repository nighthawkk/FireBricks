ii=1
s=0
def aaaa(url):
    import requests
    import httplib
    import re
    import evaluate
    import time
    import socket
    import subprocess
    
    start = finish = time.time()
    f = open('url.txt','w')

    def patch_send():
        old_send= httplib.HTTPConnection.send
        
        def new_send( self, data ):
            global ii,s
            if ii==1:
                
                
                #print(data)
                t = data.find('GET')
                t=t+4
                s = data[t:].find('HTTP')
                xx = data[t:t+s-1]
                f.write(xx)
            ii+=1
            
            return old_send(self, data) #return is not necessary, but never hurts, in case the library is changed
        httplib.HTTPConnection.send= new_send
    i=0
    flag=0

    while finish-start <30:
        patch_send()
        #url = raw_input("enter url")
        requests.get(url)
        finish = time.time()
        print("Request at "+str(finish-start)+" sec")
        if  i>10:
            f.close()
            f = open('url.txt','r')
            for line in f:
                s = evaluate.pred(line)
                #print(s)
                if s==1:
                    print('Bulk Data Breach Detected')
                    ip=socket.gethostbyname(socket.gethostname())
                    print (ip+" :IP Blocked")
                    #subprocess.call(['runas', '/user:Administrator', 'netsh advfirewall firewall add rule name="IP Block" dir=in interface=any action=block remoteip='+ip])
                    f = open('C://xampp/htdocs/cap/blockip.txt','a+')
                    f.write(ip+' ')
                    f.close()


                    flag=1
                    break
        if flag:
            break
        i+=1
