# coding: utf-8
from base64 import b64decode, b64encode
from PIL import Image
from io import BytesIO
from os import stat
from IPython.nbformat import read, write


def compress(filename, img_width=1024, img_format='jpeg', output_filename=None):
    """Compress images in IPython notebooks.

    Parameters
    ----------
    filename : string
        Notebook to compress. Will take any notebook format.
    img_width : int
        Which width images should be resized to.
    img_format : string
        Which compression to use on the images, valid options are
        *png* and *jpeg* (**requires libjpeg**).
    output_filename : string
        If you do not want to overwrite your existing notebook, supply an
        filename for the new compressed notebook.

    Returns
    -------
    int
        Size of new notebook in bytes.
    """
    orig_filesize = stat(filename).st_size

    # compress images
    nb = read(filename, as_version=4)
    outputs = [cell.get('outputs', []) for cell in nb['cells']]
    # omit empty outputs
    outputs = [o for o in outputs if len(o)]
    # flatten
    outputs = [o for lines in outputs for o in lines]
    for output in outputs:
        data = output.get('data', {})
        if not data:
            continue
        keys = data.keys()
        for key in keys:
            if 'image' in key:
                string = ''.join(data[key])
                bytes_img = b64decode(string)
                io_img = BytesIO(bytes_img)
                img = Image.open(io_img)
                factor = float(img_width) / img.size[0]
                if factor < 1:
                    # only resize large images
                    new_size = [int(s*factor+0.5) for s in img.size]
                    img = img.resize(new_size)
                out = BytesIO()
                img.save(out, img_format)
                out.seek(0)
                b64_img = b64encode(out.read())
                del data[key]
                data['image/' + img_format] = _chunkstring(b64_img, 77)

    # save notebook
    if not output_filename:
        output_filename = filename
    try:
        output_format = nb.metadata.orig_nbformat
    except AttributeError:
        output_format = 4
    write(nb, output_filename, version=output_format)

    # calculate bytes saved
    bytes_saved = orig_filesize - stat(output_filename).st_size
    if bytes_saved <= 0:
        print('Warning: ipynbcompress did not compress notebook, %s bytes gained' % bytes_saved)
    return bytes_saved


def _chunkstring(string, length):
    "Chops a string into chunks."
    return [string[0+i:length+i] for i in range(0, len(string), length)]
