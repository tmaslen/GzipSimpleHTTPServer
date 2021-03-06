#!/usr/bin/python
"""Simple HTTP Server.

This module builds on BaseHTTPServer by implementing the standard GET
and HEAD requests in a fairly straightforward manner.

"""

PORT = 9999

__version__ = "0.3"

import BaseHTTPServer
from MaslenRequestHandler import MaslenRequestHandler

def test(HandlerClass = MaslenRequestHandler, ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)

if __name__ == '__main__':
    test()
