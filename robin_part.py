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
    teamrobot_TECS.sendHearEvent(client, "Robin, I presume?")
    to_speak = teamrobot_TECS.getSpeakEvent(client)
    if to_speak:
        print "I say: {}".format(to_speak)
    else:
        print "Misunderstood"
    client.disconnect()
