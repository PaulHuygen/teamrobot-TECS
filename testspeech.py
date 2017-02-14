#!/usr/bin/python2.7
# coding: utf8
import sys,glob
import datetime

from de.dfki.tecs.misc import *
from de.dfki.tecs.ps.PSFactory import PSFactory
from de.dfki.tecs.discovery.DiscoveryTree import *
from genpy.rise.core.utils.tecs.constants import *
from genpy.rise.core.utils.tecs.ttypes import *

import teamrobot_TECS

if __name__ == "__main__":
    client = teamrobot_TECS.makeTECSclient()
    client.connect()
    while True:
        speechs = teamrobot_TECS.get_VU_processed(client)
        if speechs == "StopIt":
            print "Stop."
            client.disconnect()
            sys.exit()
        print "I say: {}".format(speechs)
 
