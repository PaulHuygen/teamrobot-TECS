#!/usr/bin/python2.7
# coding: utf8

##
# The Creative Commons CC-BY-NC 4.0 License
#
# http://creativecommons.org/licenses/by-nc/4.0/legalcode
#
# Creative Commons (CC) by DFKI GmbH
#  - Christian Bürckert <Christian.Buerckert@DFKI.de>
#  - Yannick Körber <Yannick.Koerber@DFKI.de>
#  - Magdalena Kaiser <Magdalena.Kaiser@DFKI.de>

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.
#
import sys,glob
import datetime

from de.dfki.tecs.misc import *
from de.dfki.tecs.ps.PSFactory import PSFactory
from de.dfki.tecs.discovery.DiscoveryTree import *

#import generated user space source
# from genpy.de.dfki.tecs.examples.helloworld.constants import *
# from genpy.de.dfki.tecs.examples.helloworld.ttypes import *
from genpy.rise.core.utils.tecs.constants import *
from genpy.rise.core.utils.tecs.ttypes import *

# TECSserver_url = 'localhost'
# TECSserver_port = 9000
TECSserver_url = '139.162.151.201'
TECSserver_port = 1237

def makeTECSclient():
    "Generate a TECS client and subscribe on two events"
    uri = PSFactory.createURI('python-client', TECSserver_url, TECSserver_port)
    client = PSFactory.createPSClient(uri)
    client.subscribe("HearingEvent")
    client.subscribe("SpeakingEvent")
    return client


def sendHearEvent(client, s):
    "submit speech that Robin heard"
    hearingevent =  HearingEvent( HeardSpeech = s )
    client.send(".*", "HearingEvent", hearingevent)

def getHearEvent(client):
    "receive a speech event that Robin heard"
    while (client.isConnected()):
        while (client.canRecv()):
            evt = client.recv()
            if (evt.is_a("HearingEvent")):
                    he = HearingEvent()
                    evt.parseData(he)
 #                   client.disconnect()
                    return he.HeardSpeech

def HearEvents(client):
    "receive a list of speech events that Robin heard"
    while (client.isConnected()):
        while (client.canRecv()):
            evt = client.recv()
            if (evt.is_a("HearingEvent")):
                    he = HearingEvent()
                    evt.parseData(he)
 #                   client.disconnect()
                    yield he.HeardSpeech




def sendSpeakingEvent(client, s):
    "submit speech that Robin ought to speak"
    speakingevent =  SpeakingEvent( SpeakSpeech = s )
    client.send(".*", "SpeakingEvent", speakingevent)

def getSpeakEvent(client):
    "receive speech that Robin ought to speak"
    while (client.isConnected()):
        while (client.canRecv()):
            evt = client.recv()
            if (evt.is_a("SpeakingEvent")):
                    se = SpeakingEvent()
                    evt.parseData(se)
 #                   client.disconnect()
                    return se.SpeakSpeech



if __name__ == "__main__":
    client = makeTECSclient()
    client.connect()
    sendHearEvent(client, "Robin, I presume?")
    heard = getHearEvent(client)
    if heard:
        print "heard: {}".format(heard)
    else:
        print "Misunderstood"
    client.disconnect()



