import unittest
import os
from GzipSimpleHTTPServer.Mixin import Mixin
# from unittest.mock import Mock
from mock import MagicMock, PropertyMock

THIS_DIR = os.path.dirname(os.path.abspath(__file__)).replace('/tests', '/')

def getFixture(path):
    with open(path, 'r') as file:
        fileContents=file.read().replace('\n', '')
    return fileContents

def getFixtureMinimized(path):
	return ''.join(getFixture(path).split())

class GzipSimpleHTTPRequestHandlerTestCase(unittest.TestCase):
	def test_translate_path(self):
		m = Mixin()
		self.assertEqual(m.translate_path("test.html"), THIS_DIR + "test.html")
		self.assertEqual(m.translate_path("test.html?foo=bar"), THIS_DIR + "test.html")
		self.assertEqual(m.translate_path("test.html#anchor"), THIS_DIR + "test.html")

	def test_guess_type(self):
		p = PropertyMock(return_value={
			".html": "text/html",
			"":""
		})
		Mixin.extensions_map = p
		m = Mixin()
		self.assertEqual(m.guess_type("test.html"), "text/html")
		self.assertEqual(m.guess_type("test.HTML"), "text/html")
		self.assertEqual(m.guess_type("test.madeup"), "")

	def test_list_directory(self):
		fixture = getFixtureMinimized(THIS_DIR+"tests/fixtures/test_list_directory.html")

		p = PropertyMock(return_value="/tests/manual-test")
		Mixin.path = p
		Mixin.send_response = MagicMock()
		Mixin.send_header = MagicMock()
		Mixin.end_headers = MagicMock()
		m = Mixin()
		f = m.list_directory(THIS_DIR+"tests/manual-test")

		self.assertEqual(''.join(f.getvalue().split()), fixture)
