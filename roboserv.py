# roboserv -- server to communicate with TECS server in Team-robot project
from flask import Flask, request, render_template

import sys,glob
import datetime

from de.dfki.tecs.misc import *
from de.dfki.tecs.ps.PSFactory import PSFactory
from de.dfki.tecs.discovery.DiscoveryTree import *
from genpy.rise.core.utils.tecs.constants import *
from genpy.rise.core.utils.tecs.ttypes import *

import teamrobot_TECS


app = Flask(__name__)

VU_processed = "Hello World"

@app.route("/")
def hello():
    return VU_processed

@app.route("/send" , methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        VU_processed = request.form['VU_processed']
#        print "Got: {}".format(VU_processed)
        client = teamrobot_TECS.makeTECSclient()
        client.connect()
        teamrobot_TECS.send_VU_processed(client, VU_processed)
        client.disconnect()
#        print "sent: {}".format(VU_processed)
        return "Received: {}".format(VU_processed)
    else:
        return render_template('sendtempl.html')


@app.route("/waitfor" , methods=['GET'])
def waitfor():
    client = teamrobot_TECS.makeTECSclient()
    client.connect()
    VU_processed = teamrobot_TECS.get_ASR_text(client)
    return VU_processed




if __name__ == "__main__":
    app.run()

