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
        print "Not enough arguments."
        print "Usage: python testsend (ASR | VU)"
        sys.exit(4)
    client = teamrobot_TECS.makeTECSclient()
    client.connect()
    if sys.argv[1] == "ASR":
        print "Send ASR string."
        teamrobot_TECS.send_ASR_text(client, "Aap, noot, Mies")
    elif sys.argv[1] == "VU":
        print "Send VU string."
        teamrobot_TECS.send_VU_text(client, "Maan zaag Fien vier")
    else:
        print "Usage: python testsend (ASR | VU)"
    client.disconnect()
 
