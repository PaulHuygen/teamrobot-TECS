# For python 2.7
# 20170214 Paul Huygen
# Reads standard in and sends to roboteam tecs server.

import sys,glob
import datetime
import os

from de.dfki.tecs.misc import *
from de.dfki.tecs.ps.PSFactory import PSFactory
from de.dfki.tecs.discovery.DiscoveryTree import *
from genpy.rise.core.utils.tecs.constants import *
from genpy.rise.core.utils.tecs.ttypes import *

import teamrobot_TECS

if __name__ == "__main__":
    save_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    client = teamrobot_TECS.makeTECSclient()
    client.connect()
    rec_string = teamrobot_TECS.get_ASR_text(client)
    client.disconnect()
    sys.stdout = save_stdout
    print rec_string
