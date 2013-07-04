import sys
import json
from stack import Stack
from messages import Message

from pprint             import pprint
from twisted.internet   import reactor
from twisted.python     import log
from autobahn.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS

class ScalableServerProtocol(WebSocketClientProtocol):
    _connected = False
    _user = 'Oby-chan'
    _history = Stack(True)

    def parseMessage(self, message):

        if( type(message) != dict ):
            try:
                message = json.loads(message)
            except ValueError:
                pass

        if( type(message) != dict):
            message = {
                'user': _user,
                'message': message
            }

        Message.generate(message)

        return message

    def send(self, message):
        message = self.parseMessage(message)

        if(_history.contains(message) == False):

            text = json.dump(message)
            self.sendMessage(text)
            _history.add(message)

    def dump(self, message):
        pprint(message)

    # Default functions

    def onOpen(self):
        connected = True
        
    def onMessage(self, msg, binary):
        parsedMessage = self.parseMessage(msg)

        if(_history.contains(parsedMessage) == False):
            self.dump(parsedMessage)
            _history.add(parsedMessage)


if __name__ == '__main__':

    host = 'localhost' #"jpd.es"
    port = 8800

    address = 'ws://' + host + ':' + str(port)

    factory = WebSocketClientFactory(address, debug = True, debugCodePaths = True)
    factory.protocol = ScalableServerProtocol

    connectWS(factory)

    reactor.run()
