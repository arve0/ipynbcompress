"""
Tests for `ipynbcompress`.
"""
import pytest
from ipynbcompress import *
from py import path


@pytest.fixture
def notebooks(tmpdir):
    "v3 and v4 notebook in tmpdir. Returns list of py.path object."
    testdir = path.local(__file__).dirpath()
    n3 = testdir.join('notebook3.ipynb')
    n4 = testdir.join('notebook4.ipynb')
    n3.copy(tmpdir)
    n4.copy(tmpdir)
    return tmpdir.listdir()


def test_stitch(tmpdir, notebooks):
    "It should compress a notebook."
    for notebook in notebooks:
        outfile = tmpdir.join('out.ipynb')
        saved = compress(notebook.strpath, 800, 'jpeg', outfile.strpath)

        # it should not gain in size
        assert saved > 0

        # output file should exists
        assert outfile.check()

        outfile.remove()
