import click
import utils


def common(OUTPUT, args):

    data = utils.render(utils.TEMPLATES.MAIN, **args)
    if OUTPUT:
        open(OUTPUT, 'w').write(data)
        click.echo("[*] Stored in file '{}'".format(OUTPUT))
    else:
        click.echo(data)
