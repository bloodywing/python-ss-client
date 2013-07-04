import sys
import json

from pprint             import pprint
from twisted.internet   import reactor
from twisted.python     import log
from autobahn.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS


#j_in = r'["foo", {"bar": ["baz", null, 1.0, 2]}]'
#j_out = json.loads(j_in)

#print j_in
#print j_out
#print json.dumps(j_out)

class ScalableServerProtocol(WebSocketClientProtocol):
    connected = False
    user = 'Oby-chan'

    def parseMessage(self, message):

        if( type(message) != dict ):
            try:
                message = json.loads(message)
            except ValueError:
                pass

        if( type(message) != dict):
            message = {
                'user': user,
                'message': message
            }

        return message

    def send(self, message):
        message = self.parseMessage(message)
        text = json.dump(message)

        self.sendMessage(text)

    def dump(self, message):
        pprint(message)

    # Default functions

    def onOpen(self):
        connected = True
        
    def onMessage(self, msg, binary):
        parsedMessage = self.parseMessage(msg)

        self.dump(parsedMessage)


if __name__ == '__main__':

    host = 'localhost' #"jpd.es"
    port = 8800

    address = 'ws://' + host + ':' + str(port)

    factory = WebSocketClientFactory(address, debug = True, debugCodePaths = True)
    factory.protocol = ScalableServerProtocol

    connectWS(factory)

    reactor.run()
