import io

import click

from tree import trie



@click.command()
@click.argument("file", type=click.File())
def cli(file: io.TextIOBase) -> None:
    click.echo(trie.make_trie(file.read(), "\n").to_string(ascii_only=False))
