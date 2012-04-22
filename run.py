import irc

manager = irc.Manager(irc.Config('irc.json'))
manager.init(10000)

