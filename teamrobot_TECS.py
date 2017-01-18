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

from de.dfki.tecs.misc import *
from de.dfki.tecs.ps.PSFactory import PSFactory
from de.dfki.tecs.discovery.DiscoveryTree import *

#import generated user space source
# from genpy.de.dfki.tecs.examples.helloworld.constants import *
# from genpy.de.dfki.tecs.examples.helloworld.ttypes import *
from genpy.rise.core.utils.tecs.constants import *
from genpy.rise.core.utils.tecs.ttypes import *


def discovery_example():
	#Open a Connection with id python-discovery-client  
	client = PSFactory.createPSClient("python-discovery-client")
	client.subscribe("HelloWorldEvent")
	client.connect()

	#Test sending
	print ("Sending HelloWorldEvent");
	client.send(".*", "HelloWorldEvent", HelloWorldEvent('Hello World'))

	#Test receiving
	while (client.isConnected()):
		while (client.canRecv()):
			evt = client.recv()
			print ("Received: %s from %s addressed to %s at %d" % (evt.getEtype() ,evt.getSource(), evt.getTarget(), evt.getTime()));
			#Interpret Data if it's HelloWorldEvent
			if (evt.is_a("HelloWorldEvent")):
				hwe = HelloWorldEvent()
				evt.parseData(hwe)
				print ("Message: %s\n" % hwe.message)
				client.disconnect()
				break #otherwise canRecv would throw an error because disconnected.
		
	print ("Successfully shutdown and stopped")


def uri_example():
	uri = PSFactory.createURI('python-client', 'localhost', 9000)

	client = PSFactory.createPSClient(uri)
	client.subscribe("HelloWorldEvent")
	client.connect()


	#Test sending
	print ("Sending HelloWorldEvent");
	client.send(".*", "HelloWorldEvent", HelloWorldEvent('Kijk nou eens!'))

	#Test receving
	while (client.isConnected()):
		while (client.canRecv()):
			evt = client.recv()
			print ("Received: %s from %s addressed to %s at %d" % (evt.getEtype() ,evt.getSource(), evt.getTarget(), evt.getTime()));
			#Interpret Data if it's HelloWorldEvent
			if (evt.is_a("HelloWorldEvent")):
				hwe = HelloWorldEvent()
				evt.parseData(hwe)
				print ("Message: %s\n" % hwe.message)
				client.disconnect()
				break
		
	print ("Successfully shutdown and stopped")


uri_example()
# discovery_example()


#while True:
#	uri = PSFactory.discoverURI("test", 1000, DiscoveryTree.ALL)
	#print uri
