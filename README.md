# teamrobot-TECS

Simple, rudimentary client to exchange strings over a TECS server.
Script `teamrobot-TECS.py` contains methods for the
communication. Scripts `vu_part.py` and `robin_part.py` are demo examples
that show usage.

# Demo Usage

1. Clone this and make sure you use Python 2.7.
2. Install libtecs in your Python distribution if you have not done
   that yet:
    * `wget https://cloud.dfki.de/owncloud/index.php/s/aCcdLNm0jY2b04T/download?path=%2Flibtecs%2Fpy&files=libtecs-2.0.4.tar.gz`
    * `mv download\?path\=%2Flibtecs%2Fpy\&files\=libtecs-2.0.4.tar.gz libtecs-2.0.4.tar.gz`
    *  `tar -xzf libtecs-2.0.4.tar.gz` 
    * `tar -xzf libtecs-2.0.4.tar.gz`
    * `cd libtecs-2.0.4/`
    * `python setup.py install`
3. Compile the thrift file. Do: `thrift -gen py thrift/VPRO_message_types_VU.thrift`
4. Do `ln -s gen-py genpy`.
5. Start the TECS server if you have not done that yet.
6. Fill in the URL and the port of the server in `teamrobot_TECS.py`
7. Do `python vu_part.py`.
8. In another terminal do `python robin_part.py` and see that a
   communication has taken place.

# Python flask app

The current TECS software needs Python 2.7 and that causes problems
when other modules that you want to use are dependent of
Python 3.x. To alleviate this problem, a Python flask app has been
made that waits for `ASR_text` strings and sends `VU_processed`
strings (see the thrift file). Unfortunately it
is not yet reliable and tend to "hang". Use it as follows in test mode:

1. Make sure you have a python 2.7 environment with libtecs installed
   (see above).
2. Do the following in a terminal:
    * `export FLASK_APP=roboserv.py`
    * `export FLASK_DEBUG=1`
	* `flask run`
3. Open `http://localhost:5000` in a browser. This will print "Hello
   world".
4. Open `http://localhost:5000/send` in a browser. This will print a
   form to send a string to the TECS server.
5. Open `http://localhost:5000/waitfor` in a browser. This will wait
   until somebody sends a string to the server and then print that string.
   
# Bash script

Another solution for the Python 3 vs. Python 2 problem are two Bash
scripts that send resp, reveives a string from the TECS server. Use
them as follows:

1. Make sure you have e.g. a virtual python 2.7 environment with libtecs installed
   (see above).
2. Copy bash scripts `get_ASR_text` and `send_VU_processed` to a
   location where they can be found.
3. Edit the two scripts:
    * Set the location of this package in variable `SCRIPTDIR`
    * "Source" the correct Python virtual environment.
4. Call the script in an approtriate way in your Python program (eg
   using the `Popen` directive).
 


# Files

* `VPRO_message_types_VU.thrift`: Thrift file
* `teamrobot_TECS.py`: Python file to be imported.
* `__init__.py`: (empty) init file.
* `robin_part.py`: example to send an `ASR_text` string to the TECS
  server and receive a corresponding `VU_processed` string in return.
* `vu_part.py`: example that receives an `ASR_text` string and then sends a
  `VU_processed` string back.
* `testsend.py`: Send a string to the server. It expects "ASR" or "VU"
  as argument.
* `testreceive.py`: Receive strings to the server. It expects "ASR" or "VU"
  as argument.

