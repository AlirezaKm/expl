from jinja2 import Template
import os

"""Get Current Directory"""
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')


class TEMPLATES:
    """
    Store Template names
    """
    MAIN = 'template'


def load_template(filename: str, templates_dir: str, extension: str) -> str:
    """
    Load Template from templates

    :param filename: filename in templates path
    :param templates_dir: path of templates (default: xpl_address/templates)
    :param extension: extension of input file (default: 'template')
    :return: content of template file
    """
    try:
        return open(os.path.join(
            templates_dir,
            "{}.{}".format(filename, extension)
        ), 'r').read()
    except Exception as e:
        print(e)
        exit(-1)


def render(template: str, templates_dir: str = TEMPLATES_DIR, extension: str = 'jinja2', **args):
    # Load a template
    data = load_template(template, templates_dir, extension)

    # Create a Jinja Template
    template = Template(data)

    # Render Template by its arguments
    return template.render(**args)
