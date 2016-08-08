#!/usr/bin/python
"""Simple HTTP Server.

This module builds on BaseHTTPServer by implementing the standard GET
and HEAD requests in a fairly straightforward manner.

"""


__version__ = "0.3"

import BaseHTTPServer
from GzipSimpleHTTPRequestHandler import GzipSimpleHTTPRequestHandler

def test(HandlerClass = GzipSimpleHTTPRequestHandler, ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()