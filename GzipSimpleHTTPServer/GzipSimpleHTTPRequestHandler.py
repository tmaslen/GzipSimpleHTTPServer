import BaseHTTPServer
import os
import mimetypes
import shutil
import struct
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
from Mixin import Mixin
import sys
import gzip

__all__ = ["GzipSimpleHTTPRequestHandler"]

gzipContentSetting = 'default'

for arg in sys.argv:
    if arg == '--gzipeverything':
        gzipContentSetting = 'gzip'

def gzipFile(content):
    out = StringIO()
    f = gzip.GzipFile(fileobj=out, mode='w', compresslevel=5)
    f.write(content)
    f.close()
    return out.getvalue()

def isFileGzipped(f):
    first_byte = f.read(1)
    f.seek(0)
    return ord(first_byte) == 31

def processContentDefault(isFileGzippedResult, content, ref):
    if (isFileGzippedResult):
        ref.send_header("Content-Encoding", "gzip")
    return content

def gzipAllContent(isFileGzippedResult, content, ref):
    ref.send_header("Content-Encoding", "gzip")
    if (isFileGzippedResult):
        return content
    else:
        return gzipFile(content)


def processContent(gzipContentSetting, content, ref, isFileGzippedResult):
    
    processUsing = {
        'default': processContentDefault,
        'gzip': gzipAllContent
    }

    return processUsing[gzipContentSetting](isFileGzippedResult, content, ref)


class GzipSimpleHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler, Mixin):

    """Simple HTT request handler with GET and HEAD commands.

    This serves files from the current directory and any of its
    subdirectories.  The MIME type for files is determined by
    calling the .guess_type() method.

    The GET and HEAD requests are identical except that the HEAD
    request omits the actual contents of the file.

    """

    if not mimetypes.inited:
        mimetypes.init() # try to read system mime.types
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'application/octet-stream', # Default
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
        })

    def do_GET(self):
        """Serve a GET request."""
        content = self.send_head()
        if content:
            self.wfile.write(content)

    def do_HEAD(self):
        """Serve a HEAD request."""
        content = self.send_head()

    def send_head(self):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.

        Return value is either a file object (which has to be copied
        to the outputfile by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.

        """
        path = self.translate_path(self.path)
        print("Serving path '%s'" % path)
        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path).read()
        ctype = self.guess_type(path)
        try:
            # Always read in binary mode. Opening files in text mode may cause
            # newline translations, making the actual size of the content
            # transmitted *less* than the content-length!
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        first_byte = f.read(1)
        f.seek(0)
        isFileGzippedResult = isFileGzipped(f)
        fs = os.fstat(f.fileno())
        raw_content_length = fs[6]
        content = processContent(gzipContentSetting, f.read(), self, isFileGzippedResult)
        compressed_content_length = len(content)
        f.close()
        self.send_header("Content-Length", max(raw_content_length, compressed_content_length))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return content