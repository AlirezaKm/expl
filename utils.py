import os

"""Get Current Directory"""
BASE_DIR = os.path.join(os.path.dirname(__file__), 'templates')


class TEMPLATES:
    """
    Store Template names
    """
    COMMON = 'common'
    LOCAL  = 'local'
    REMOTE = 'remote'


def load_template(filename: str, base: str = BASE_DIR, extension: str = 'template') -> str:
    """
    Load Template from templates

    :param filename: filename in templates path
    :param base: path of templates (default: xpl_address/templates)
    :param extension: extension of input file (default: 'template')
    :return: content of template file
    """
    try:
        return open(os.path.join(
            base,
            "{}.{}".format(filename, extension)
        ), 'r').read()
    except Exception as e:
        print(e)
        exit(-1)
