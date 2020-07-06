from commands._base import common
import click


@click.group('Remote')
def remote():
    pass


@remote.command('remote', help='Generate Remote Template')
@click.option('-a', '--arch', 'ARCH', default='x86_64', help='Architecture of Executable File', show_default=True)
@click.option('--os', 'OS', default='linux', help='OS of Executable File', show_default=True)
@click.option('-e', '--endian', 'ENDIAN', default='little', help='OS of Executable File', show_default=True)
@click.option('-l', '--loglevel', 'LOG_LEVEL', default='info', help='Log Level of pwntools', show_default=True)
@click.option('--libc', 'LIBC', help='Address of LIBC')
@click.option('--heap', 'HEAP', help='Adding heap functions', is_flag=True, default=False)
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
        HEAP,
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

    if HEAP:
        args.update(HEAP=HEAP)

    common(OUTPUT, args)
