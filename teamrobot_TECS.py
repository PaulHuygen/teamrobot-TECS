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


def makeTECSclient():
    "Generate a TECS client and subscribe on two events"
    uri = PSFactory.createURI('python-client', 'localhost', 9000)
    client = PSFactory.createPSClient(uri)
    client.subscribe("HearingEvent")
    client.subscribe("SpeakingEvent")
    return client

def sendHearEvent(client, s):
    hearingevent =  HearingEvent( HeardSpeech = s )
    client.send(".*", "HearingEvent", hearingevent)

def getHearEvent(client):
    while (client.isConnected()):
        while (client.canRecv()):
            evt = client.recv()
            if (evt.is_a("HearingEvent")):
                    he = HearingEvent()
                    evt.parseData(he)
 #                   client.disconnect()
                    return he.HeardSpeech

def sendSpeakingEvent(client, s):
    speakingevent =  SpeakingEvent( SpeakSpeech = s )
    client.send(".*", "SpeakingEvent", speakingevent)

def getSpeakEvent(client):
    while (client.isConnected()):
        while (client.canRecv()):
            evt = client.recv()
            if (evt.is_a("SpeakingEvent")):
                    se = SpeakingEvent()
                    evt.parseData(se)
 #                   client.disconnect()
                    return se.SpeakSpeech


def uri_example():

        client = makeTECSclient()
        client.connect()
	#Test sending
	print ("Sending expression heard by robot");
        sendHearEvent(client, "Robin, I presume?")
#	client.send(".*", "HearingEvent", hearingevent)

	#Test receving
        heard = getHearEvent(client)
        if heard:
            print "heard: {}".format(heard)
        else:
            print "Misunderstood"
        client.disconnect()
#	uri = PSFactory.createURI('python-client', 'localhost', 9000)
#
#	client = PSFactory.createPSClient(uri)
#	client.subscribe("HearingEvent")
#	client.connect()
#	while (client.isConnected()):
#		while (client.canRecv()):
#			evt = client.recv()
#			print ("Received: %s from %s addressed to %s at %d" % (evt.getEtype() ,evt.getSource(), evt.getTarget(), evt.getTime()));
#			#Interpret Data if it's HearingEvent
#			if (evt.is_a("HearingEvent")):
#				he = HearingEvent()
#				evt.parseData(he)
#				print ("Message: %s\n" % he.HeardSpeech)
#				client.disconnect()
#				break
#			elif (evt.is_a("RobotPresenterData")):
#				rbe = RobotPresenterData()
#				evt.parseData(rbe)
#				print ("Speaker: %s\n" % rbe.metadata_speaker)
#				client.disconnect()
#				break
#        client.disconnect()
#	print ("Successfully shutdown and stopped")


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



