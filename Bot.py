'''
Created on 22 Apr 2012

@author: Pure_
'''

import socket

class Bot(object):
    
    def __init__(self, hostname, port, socket_buffer, user, nick, channels):
        bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bot.connect(hostname, port)
        
        bot.send('USER ' + user)
        bot.send('NICK ' + nick)
        
        for channel in channels:
            bot.send('JOIN ' + channel)
        
        while True:
            s = bot.recv(socket_buffer)
            
            if s.startswith(":"):
                s = s[:1]
                
            if s.startswith("PING"):
                bot.send(s.replace("PING", "PONG"))