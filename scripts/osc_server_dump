#!/usr/bin/env python

import sys
from OSC import OSCServer
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-H", "--host", dest="host", default='0.0.0.0')
parser.add_option("-p", "--port", dest="port", default=8000)
parser.add_option("-t", "--target", dest="target", default='/1/test')

(options, args) = parser.parse_args()

server = OSCServer((options.host, options.port))


def do_test(addr, tags, data, client_address):
    print addr, tags, data, client_address

server.addMsgHandler(options.target, do_test)

if len(sys.argv) < 2:
    print "You need some arguments, try -h"
else:
    server.serve_forever()
