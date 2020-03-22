import click
from .local import local
from .remote import remote
from .both import both

cli = click.CommandCollection(sources=[
    local,
    remote,
    both,
])
