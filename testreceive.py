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
    if len(sys.argv) <= 1:
        print "Usage: python testreceive (ASR | VU)"
        sys.exit(4)
    client = teamrobot_TECS.makeTECSclient()
    client.connect()
    while True:
        if sys.argv[1] == "ASR":
            print "Wait for ASR string"
            rets =  teamrobot_TECS.get_ASR_text(client)
        elif sys.argv[1] == "VU":
            print "Wait for VU string"
            rets = teamrobot_TECS.get_VU_processed(client)
        else:
            print "I don't understand: {}".format(sys.argv[1])
            print "Usage: python testsend (ASR | VU)"
            sys.exit(4)
        if rets == "StopIt":
            print "Stop."
            break
        print rets
    client.disconnect()
    sys.exit()
 
