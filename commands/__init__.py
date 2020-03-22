import click
from .local import local

cli = click.CommandCollection(sources=[
    local,
])
