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
    client.subscribe("ASR_text")
    client.subscribe("VU_processed")
    return client


def send_ASR_text(client, s):
    "submit speech that Robin heard"
    hearingevent =  ASR_text( json_structure = s )
    client.send(".*", "ASR_text", hearingevent)

def get_ASR_text(client):
    "receive a speech event that Robin heard"
    while (client.isConnected()):
        while (client.canRecv()):
            evt = client.recv()
            if (evt.is_a("ASR_text")):
                    he = ASR_text()
                    evt.parseData(he)
 #                   client.disconnect()
                    return he.json_structure

def get_ASR_texts(client):
    "receive a list of speech events that Robin heard"
    while (client.isConnected()):
        while (client.canRecv()):
            evt = client.recv()
            if (evt.is_a("ASR_text")):
                    he = ASR_text()
                    evt.parseData(he)
 #                   client.disconnect()
                    yield he.json_structure




def send_VU_processed(client, s):
    "submit speech that Robin ought to speak"
    speakingevent =  VU_processed( json_structure = s )
    client.send(".*", "VU_processed", speakingevent)

def get_VU_processed(client):
    "receive speech that Robin ought to speak"
    while (client.isConnected()):
        while (client.canRecv()):
            evt = client.recv()
            if (evt.is_a("VU_processed")):
                    se = VU_processed()
                    evt.parseData(se)
 #                   client.disconnect()
                    return se.json_structure



if __name__ == "__main__":
    client = makeTECSclient()
    client.connect()
    send_VU_processed(client, "Robin, I presume?")
    heard = get_ASR_text(client)
    if heard:
        print "heard: {}".format(heard)
    else:
        print "Misunderstood"
    client.disconnect()



