# teamrobot-TECS

Simple, rudimentary client to exchange strings over a TECS server.
Script `teamrobot-TECS.py` contains methods for the
communication. Scripts `vu_part.py` and `robin_part.py` are demo examples
that show usage.

# Demo Usage

1. Clone this and make sure you use Python 2.7.
2. Install libtecs in your Python distribution if you have not done
   that yet:
      ```wget https://cloud.dfki.de/owncloud/index.php/s/aCcdLNm0jY2b04T?path=%2Flibtecs%2Fpy~
	  tar -xzf libtecs-2.0.4.tar.gz
	  cd libtecs-2.0.4/
	  python setup.py install
	   ``` 
3. Compile the thrift file. Do: `thrift -gen py thrift/robin_speech.thrift`.
4. Do `ln -s gen-py genpy`.
5. Start the TECS server if you have not done that yet.
6. Fill in the URL and the port of the server in `teamrobot_TECS.py`
7. Do `python vu_part.py`.
8. In another terminal do 'python robin_part.py' and see that a
   communication has taken place.


# Files

* thrift/robin_speech.thrift: Thrift file
* teamrobot_TECS.py: Python file to be imported.
* __init__.py: (empty) init file.
* robin_part.py: example to send strings related to what Robin heard
  and to receive strings related to what Robin is supposed to speakout.
* vu_part.py: example that receives what Robin heard and sends what
  Robin ought to reply.


