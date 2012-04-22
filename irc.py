import socket
import json

class Config:
    def __init__(self, cfgname):
        self._rawcfg = json.loads(open(cfgname).read())

    def get_user(self):
        return self._rawcfg['user']

    def get_nick(self):
        return self._rawcfg['nick']

    def get_servers(self):
        return self._rawcfg['servers']


class Parser:
    def parse_normal(self, line):
        """Parse line as a normal IRC message"""
        return

    def parse_misc(self, line):
        """Parse line as a miscellaneous message"""
        return

    def parse(self, line):
        """Parse line according to the IRC specification"""
        return


class Manager:
    def __init__(self, cfg):
        self._config = cfg
        self._bots = []
    
    def init(self, rejoin):
        """Initiates the manager.

        Bots attempt to reconnect after rejoin seconds
        """
        # TODO: read server list in _cfg, spawn bot for each server
        return


class Bot:
    def __init__(self, nick, user):
        self._socket = socket.socket()
        self._parser = IRCParser()

    def connect(self, host, port):
        self._socket.connect(host, port)
        # TODO: Read, Parse, React
        self._socket.close()
    
