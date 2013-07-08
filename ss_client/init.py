import sys
import json
from ss_client.stack import Stack
from ss_client.messages import Message

from pprint             import pprint
from twisted.internet   import reactor
from twisted.python     import log
from autobahn.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS
from pubsub             import pub

class ScalableServerProtocol(WebSocketClientProtocol):
    _connected = False
    _user = 'Oby-chan'
    _history = Stack(True)
    _use_events = False

    def parseMessage(self, message):

        if( type(message) != dict ):
            try:
                message = json.loads(message)
            except ValueError:
                pass

        if( type(message) != dict):
            message = {
                'message': message
            }

        Message.generate(message)

        return message


    def send(self, message):
        message = self.parseMessage(message)

        text = json.dump(message)
        self.sendMessage(text)
        self._history.add(message)

    def dump(self, message):
        pprint(message)

    # Default functions

    def onOpen(self):
        connected = True
        
    def onMessage(self, msg, binary):
        parsedMessage = self.parseMessage(msg)

        if(self._history.contains(parsedMessage) == False):
            self._history.add(parsedMessage)

            if("event" in parsedMessage.keys() and self._use_events == True):
                self.trigger("evt." + parsedMessage['event'], parsedMessage)
            else:
                self.trigger("message", parsedMessage)

    # enddef

    def trigger(self, event, data):

        # data = dict
        # event = string
        
        pub.sendMessage(event, msg=data)

# ----------------------------------------------------------------------------

if __name__ == '__main__':

    host = 'localhost' #"jpd.es"
    port = 8800

    address = 'ws://' + host + ':' + str(port)

    def pdump(msg):
        if("event" in msg.keys()):
            print "Event: %s", msg['event']
        
        print msg['user'], ': ', msg['message']

    pub.subscribe(pdump, 'message')


    factory = WebSocketClientFactory(address, debug = True, debugCodePaths = True)
    factory.protocol = ScalableServerProtocol

    connectWS(factory)

    reactor.run()
