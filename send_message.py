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



def uri_example():
	uri = PSFactory.createURI('python-client', 'localhost', 9000)

	client = PSFactory.createPSClient(uri)
	client.subscribe("RobotPresenterData")
	client.connect()

        robotevent \
           =  RobotPresenterData( metadata_speaker = "Alladin" \
                                , structure_prepositional_phrases_count = 0 \
                                , structure_adjective_count = 0 \
                                , structure_non_future = 0 \
                                , structure_active_sentences = 0 \
                                , structure_personal_pronouns = 0 \
                                , structure_word_length = 0 \
                                , structure_negations = 0 \
                                , structure_adverbs = 0 \
                                , structure_passive_sentences = 0 \
                                , structure_number_of_sentences = 0 \
                                , structure_future = 0 \
                                , structure_wordcount = 0 \
                                , metadata_lang = 'nl' \
                                , metadata_timestamp = datetime.datetime.now().isoformat() \
                                , metadata_input_text = "Open u" \
                                , metadata_confidence_score = "0" \
                                , metadata_other_possible_responses = [] \
                                , metadata_people_present = [ "robot", "thin_air" ] \
                                , metadata_script_id = "testscript" \
                                , metadata_location_geometry_coordinates = [ 0.0, 0.0 ] \
                                , metadata_location_geometry_type = "Rock" \
                                , metadata_location_type = "Rock" \
                                  , metadata_location_properties_name = ["Desert"] \
                                , metadata_scene_id = "Fable" \
                                , semantic_keywords = ["lantern"] \
                                , semantic_organisations = [] \
                                , semantic_people = [] \
                                , semantic_places = [] \
                                , semantic_topics = [] \
                                , emotions_detected_emotion = [] \
                                , emotions_information_state = [] \
                                )

	#Test sending
	print ("Sending expression heard by robot");
#	client.send(".*", "HelloWorldEvent", HelloWorldEvent('Kijk nou eens!'))
	client.send(".*", "RobotPresenterData", robotevent)

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
			elif (evt.is_a("RobotPresenterData")):
				rbe = RobotPresenterData()
				evt.parseData(rbe)
				print ("Speaker: %s\n" % rbe.metadata_speaker)
				client.disconnect()
				break
		
	print ("Successfully shutdown and stopped")


uri_example()
# discovery_example()


#while True:
#	uri = PSFactory.discoverURI("test", 1000, DiscoveryTree.ALL)
	#print uri
