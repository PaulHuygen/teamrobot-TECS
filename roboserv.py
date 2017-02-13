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

speechstr = "Hello World"

@app.route("/")
def hello():
    return speechstr

@app.route("/send" , methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        speechstr = request.form['speechstr']
#        print "Got: {}".format(speechstr)
        client = teamrobot_TECS.makeTECSclient()
        client.connect()
        teamrobot_TECS.sendSpeakingEvent(client, speechstr)
        client.disconnect()
#        print "sent: {}".format(speechstr)
        return "Received: {}".format(speechstr)
    else:
        return render_template('sendtempl.html')


@app.route("/waitfor" , methods=['GET'])
def waitfor():
    client = teamrobot_TECS.makeTECSclient()
    client.connect()
    speechstr = teamrobot_TECS.getHearEvent(client)
    return speechstr




if __name__ == "__main__":
    app.run()

