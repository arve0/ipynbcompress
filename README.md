# ipynbcompress

[![build-status-image]][travis]
[![pypi-version]][pypi]
[![wheel]][pypi]

## Overview

So you have included an image with `IPython.display.Image()` and the file size
of your IPython Notebook got huge? No problem! This package will resize images
in your notebook and compress them as JPG or PNG.

## Installation

Install using `pip`...

```bash
pip install ipynbcompress
```

## Example
From command line:
```sh
$ ipynb-compress notebook4.ipynb
notebook4.ipynb: 10 megabytes decrease
```

In python:
```python
>>> import os
>>> from ipynbcompress import compress
>>> filename = '/path/to/notebook.ipynb'
>>> out = '/path/to/compressed.ipynb'
>>> # original size
... os.stat(filename).st_size
11563736
>>> # return bytes saved
... compress(filename, output_filename=out, img_width=800, img_format='jpeg')
11451545
>>> compress(filename, output_filename=out, img_width=800, img_format='png')
11205762
>>> # defaults to img_width = 1024px and jpeg compression
... compress(filename, output_filename=out)
11411377
>>> # overwrite existing notebook
... compress(filename)
11411377
```

## API reference

API reference is at http://ipynbcompress.rtfd.org.

## Development
Install dependencies and link development version of ipynbcompress to pip:
```bash
git clone https://github.com/arve0/ipynbcompress
cd ipynbcompress
pip install -r requirements.txt # install dependencies and ipynbcompress-package
```

### Testing
```bash
tox
```

### Build documentation locally
To build the documentation:
```bash
pip install -r docs/requirements.txt
make docs
```



[build-status-image]: https://secure.travis-ci.org/arve0/ipynbcompress.png?branch=master
[travis]: http://travis-ci.org/arve0/ipynbcompress?branch=master
[pypi-version]: https://pypip.in/version/ipynbcompress/badge.svg
[pypi]: https://pypi.python.org/pypi/ipynbcompress
[wheel]: https://pypip.in/wheel/ipynbcompress/badge.svg
