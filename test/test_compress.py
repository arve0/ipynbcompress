"""
Tests for `ipynbcompress`.
"""
import pytest
from ipynbcompress import *
from IPython.nbformat import validate, read, NO_CONVERT
from py import path


@pytest.fixture
def notebooks(tmpdir):
    "v3 and v4 notebook in tmpdir. Returns list of py.path object."
    testdir = path.local(__file__).dirpath()
    n3 = testdir.join('notebook3.ipynb')
    n4 = testdir.join('notebook4.ipynb')
    notebooks = tmpdir.join('notebooks').mkdir()
    n3.copy(notebooks)
    n4.copy(notebooks)
    return notebooks.listdir()


def test_compress(tmpdir, notebooks):
    "It should compress a notebook."
    for notebook in notebooks:
        outfile = tmpdir.join('out.ipynb')
        saved = compress(notebook.strpath, outfile.strpath, 800, 'jpeg')

        # it should not gain in size
        assert saved > 0

        # output file should exists
        assert outfile.check()

        validate(read(outfile.strpath, NO_CONVERT))

        outfile.remove()
