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
    for heard in teamrobot_TECS.get_ASR_texts(client):
#        heard = teamrobot_TECS.get_ASR_text(client)
        if heard:
            teamrobot_TECS.send_VU_processed(client, "And you are .... ?")
        else:
            print "Misunderstood"
