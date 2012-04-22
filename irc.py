import socket
import json

class IRCConfig:
    def __init__(self, cfgname):
        self._rawcfg = json.loads(open(cfgname).read())
    def get_user(self):
        return self._rawcfg['user']
    def get_nick(self):
        return self._rawcfg['nick']
    def get_servers(self):
        return self._rawcfg['servers']

class IRCBot:
    def set_config(self, cfg):
        self._config = cfg
        self._socket = socket.socket()
    def connect(self):
        # TODO
        self._socket.close()

