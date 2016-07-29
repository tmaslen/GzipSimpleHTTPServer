GzipSimpleHTTPServer
====================

A very simple modification of the very useful SimpleHTTPServer python script to add gzip compression.
Since this is a very simple modification made initially for personal usage. It does not check if gzip is acceptable and just assumes it is. It only sets the minimum number of headers required for it to work(Technically it does not set headers properly
for transferring files). It was tested primarily with chrome.

## Usage

Just download the python script and run it from your terminal:

```
pip install GzipSimpleHTTPServer
python -m GzipSimpleHTTPServer
````

This will start a localhost server on port 8000. You should see this in your terminal:

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

```
git clone git@github.com:tmaslen/GzipSimpleHTTPServer.git
cd GzipSimpleHTTPServer
python GzipSimpleHTTPServer
```

## Deploying new versions

Pete Down's [How to submit a package to PyPI](http://peterdowns.com/posts/first-time-with-pypi.html) is a great resource to understand what is going on here.

Register your package:

```
python setup.py register -r pypi
```

Then deploy it:

```
python setup.py sdist upload -r pypi
```