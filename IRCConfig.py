import json

class IRCConfig:
    def __init__(self, cfgname):
        self.rawcfg = json.loads(open(cfgname).read())
    def getUser(self):
        return self.rawcfg['user']
    def getNick(self):
        return self.rawcfg['nick']
    def getServers(self):
        return self.rawcfg['servers']

'''
Usage
-----

config = IRCConfig('irc.json')

print config.getUser()
print config.getNick()
print repr(config.getServers())

'''