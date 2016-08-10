MaslenDevServer
===============

A modification of the very useful SimpleHTTPServer python script (originally forked from [ksmith97](https://github.com/ksmith97)/[GzipSimpleHTTPServer](https://github.com/ksmith97/GzipSimpleHTTPServer) that adds the ability to serve compressed files.

```
python -m MaslenDevServer
```

You can also pass in a flag to force all assets served from the server to be compressed:

```
python -m MaslenDevServer 8000 --gzipeverything
```

NOTE: due to the way SimpleHTTPServer is written the first parameter has to be a port number.

## Why use this?

SimpleHTTPServer is really bloody useful. The ability to `cd` into a directory and turn it into a webserver makes development simpler as well as allowing you to organise code on your machine however you want.

There are alternatives: node projects can come with a simple HTTP server as a dependency, though you will need to add this into the project making it slightly more complex. You could also use your local copy of Apache, though now you will need to either manage symlinks or house your projects in the `httpdocs` directory.

MaslenDevServer negates having to carry a dev server as a dependency and it lets you organise your projects anyway you like. Plus it lets you work with files that have been compressed by your application, or allows you to develop with files and know what the compression will be.

## Install

Just download the python script and run it from your terminal:

```
pip install git+ssh://git@github.com/tmaslen/GzipSimpleHTTPServer.py
python -m MaslenDevServer
````

This will start a localhost server on port 8000 by default. You should see this in your terminal:

````
Serving HTTP on 0.0.0.0 port 8000 ...
````

If the port is already in use then get rid of the service using it with...

```
$ lsof -i :8000
COMMAND  PID   
Python   21500
$ kill -9 21500
```

## Developing

You can edit this project by following these steps:

```
git clone git@github.com:tmaslen/MaslenDevServer.git
cd MaslenDevServer
python MaslenDevServer
```

Then view this page in a browser:

```
http://0.0.0.0:8000/tests/manual-test
```

This project has been somewhat unit tested. Run the tests like so:

```
python -m unittest tests.test_Mixin
```
