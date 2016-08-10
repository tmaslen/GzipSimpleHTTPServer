from distutils.core import setup
setup(
  name = 'MaslenDevServer',
  packages = ['MaslenDevServer'],
  version = '0.3',
  description = 'SimpleHTTPServer that can serve gzip\'d files',
  author = 'Tom Maslen',
  author_email = 'tom_maslen@hotmail.com',
  url = 'https://github.com/tmaslen/MaslenDevServer',
  download_url = 'https://github.com/tmaslen/MaslenDevServer/tarball/0.3',
  keywords = ['web server', 'gzip'],
  classifiers = [],
  install_requires = ["Jinja2", "mock"]
)