from commands._base import common
import click
import os


@click.group('Local')
def local():
    pass


@local.command('local', help='Generate Local Template')
@click.option('-a', '--arch', 'ARCH', default='x86_64', help='Architecture of Executable File', show_default=True)
@click.option('--os', 'OS', default='linux', help='OS of Executable File', show_default=True)
@click.option('-e', '--endian', 'ENDIAN', default='little', help='OS of Executable File', show_default=True)
@click.option('-l', '--loglevel', 'LOG_LEVEL', default='info', help='Log Level of pwntools', show_default=True)
@click.option('-r', '--realpath', 'REALPATH', default=False, help='using realpath for Executable File', show_default=True)
@click.option('--libc', 'LIBC', help='Address of LIBC')
@click.option('--heap', 'HEAP', help='Adding heap functions', is_flag=True, default=False)
@click.option('-o', '--output', 'OUTPUT', help='write to output')
@click.argument('file')
def command(
        file,
        ARCH,
        OS,
        ENDIAN,
        LOG_LEVEL,
        LIBC,
        HEAP,
        OUTPUT,
        REALPATH
):
    args = dict(
        ARCH=ARCH,
        OS=OS,
        ENDIAN=ENDIAN,
        LOG_LEVEL=LOG_LEVEL,
        EXEC_FILE=file if not REALPATH else os.path.abspath(file),
        LOCAL=True,
    )

    if LIBC:
        args.update(LIBC=LIBC)

    if HEAP:
        args.update(HEAP=HEAP)

    common(OUTPUT, args)
