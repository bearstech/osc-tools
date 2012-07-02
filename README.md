OSC Tools
=========

[Open Sound Control](https://en.wikipedia.org/wiki/Open_Sound_Control)
is a simple network protocol used for connecting musical instruments and multimedia stuffs.
This protocol can be used from tiny things like Arduino to fancy interface like iPad.

Python provides a simple library, [pyOSC](https://trac.v2.nl/wiki/pyOSC), but no debug tools.

Install
-------

    python setup.py build
    sudo python setup.py install

Client
------

Message are sent via UDP, no error is return if you talk to the wrong server.

    osc_client.py -h

 * _--host_ The target host.
 * _--port_ The target port.
 * _--target_ The target path. The url like stuffs.
 * _--message_ The message. It should be JSON encoded.

Server
------

This server is simple, it just print received messages.

    osc_server_dump.py

 * _--host_ The target host.
 * _--port_ The target port.
 * _--target_ The target path. The url like stuffs.

Example
-------

In a first terminal

    osc_server_dump.py -t /1/toto

In a second terminal

    osc_client.py -t /1/toto -m 42

Licence
-------

GPLv3.
