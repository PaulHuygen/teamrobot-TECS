# For python 2.7
# 20170214 Paul Huygen
# Reads standard in and sends to roboteam tecs server.
import fileinput

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
    for line in fileinput.input():
        teamrobot_TECS.send_VU_processed(client, line)
    client.disconnect()

