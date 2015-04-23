# coding: utf-8
from json import load, dump
from base64 import b64decode, b64encode
from PIL import Image
from io import BytesIO
from os import stat


def compress(filename, img_width=1024, img_format='jpg', output_filename=None):
    """Compress images in IPython notebooks.

    Parameters
    ----------
    filename : string
        Notebook to compress.
    img_width : int
        Which width images should be resized to.
    img_format : string
        Which compression to use on the images, valid options are
        *jpg* and *png*.
    output_filename : string
        If you do not want to overwrite your existing notebook, supply an
        filename for the new compressed notebook.

    Returns
    -------
    int
        Size of new notebook in bytes.
    """
    orig_filesize = stat(filename).st_size

    with open(filename) as f:
        json = load(f)
        outputs = [cell.get('outputs', []) for cell in j['cells']]
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
                    bytes_img = b64decode(''.join(data[key]))
                    io_img = BytesIO(bytes_img)
                    img = Image.open(io_img)
                    factor = img_width / img.size[0]
                    if factor < 1:
                        # only resize large images
                        new_size = [round(s*factor) for s in img.size]
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
    with open(output_filename, 'w') as f:
        dump(json, f, indent=2, sort_keys=True)

    # calculate bytes saved
    bytes_saved = orig_filesize - stat(output_filename).st_size
    if bytes_saved <= 0:
        print('Warning: ipynbcompress did not compress notebook, %s bytes gained' % bytes_saved)
    return bytes_saved


def _chunkstring(string, length):
    "Chops a string into chunks."
    return [string[0+i:length+i] for i in range(0, len(string), length)]
