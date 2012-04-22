import socket
import json

class Configuration:
    """A general configuration class for bots and connections"""
    def __init__(self, cfgname):
        """cfgname is the JSON configuration file to use"""
        self._rawcfg = json.loads(open(cfgname).read())

    def get_user(self):
        """Gets the user parameter for bots"""
        return self._rawcfg['user']

    def get_nick(self):
        """Gets the nickname parameter for bots"""
        return self._rawcfg['nick']

    def get_servers(self):
        """Gets a list of servers for bots to be assigned to"""
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
    """Assigns bots to servers and enforces autorejoins"""
    def __init__(self, cfg):
        """cfg is the Configuration for spawned bots and contains server
        connection information
        """
        self._config = cfg
        self._bots = []
    
    def init(self, rejoin):
        """Initiates the manager.

        Bots attempt to reconnect after rejoin seconds
        """
        # TODO: read server list in _cfg, spawn bot for each server
        return


class Bot:
    """The main IRC bot class. All connection logic goes in here"""
    def __init__(self, nick, user):
        """Set user connection parameters in constructor"""
        self._nick, self._user = nick, user
        self._socket = socket.socket()
        self._parser = IRCParser()

    def connect(self, host, port=6667):
        """Connect to host on port (default: 6667)"""
        self._socket.connect(host, port)
        # TODO: Read, Parse, React
        self._socket.close()
    
