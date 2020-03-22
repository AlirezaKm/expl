import click
import utils


@click.group('Remote')
def remote():
    pass


@remote.command('remote', help='Generate Remote Template')
@click.option('-a', '--arch', 'ARCH', default='x86_64', help='Architecture of Executable File', show_default=True)
@click.option('--os', 'OS', default='linux', help='OS of Executable File', show_default=True)
@click.option('-e', '--endian', 'ENDIAN', default='little', help='OS of Executable File', show_default=True)
@click.option('-l', '--loglevel', 'LOG_LEVEL', default='info', help='Log Level of pwntools', show_default=True)
@click.option('--libc', 'LIBC', help='Address of LIBC')
@click.option('-o', '--output', 'OUTPUT', help='write to output')
@click.argument('host')
@click.argument('port')
def command(
        host,
        port,
        ARCH,
        OS,
        ENDIAN,
        LOG_LEVEL,
        LIBC,
        OUTPUT
):
    args = dict(
        ARCH=ARCH,
        OS=OS,
        ENDIAN=ENDIAN,
        LOG_LEVEL=LOG_LEVEL,
        HOST=host,
        PORT=port,
        REMOTE=True,
    )

    if LIBC:
        args.update(LIBC=LIBC)

    data = utils.render(utils.TEMPLATES.MAIN, **args)
    if OUTPUT:
        open(OUTPUT, 'w').write(data)
        click.echo("[*] Stored in file '{}'".format(OUTPUT))
    else:
        click.echo(data)
