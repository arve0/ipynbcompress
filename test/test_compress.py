"""
Tests for `ipynbcompress`.
"""
import pytest
from ipynbcompress import *
from py import path


@pytest.fixture
def notebook(tmpdir):
    "'notebook.ipynb' in tmpdir. Returns py.path object."
    n = path.local(__file__).dirpath().join('notebook.ipynb')
    n.copy(tmpdir)
    return tmpdir.join('notebook.ipynb')


def test_stitch(tmpdir, notebook):
    "It should compress a notebook."
    outfile = tmpdir.join('out.ipynb')
    saved = compress(notebook.strpath, 800, 'jpg', outfile.strpath)

    # it should not gain in size
    assert saved > 0

    # output file should exists
    assert outfile.check()
