"""Command-line interface for FC Filter Gen Tool."""

import click


@click.command()
@click.option('--name', default='World', help='Name to greet.')
@click.option('--count', default=1, help='Number of times to greet.')
def main(name, count):
    """Simple program that greets NAME COUNT times."""
    for _ in range(count):
        click.echo(f'Hello, {name}!')


if __name__ == '__main__':
    main()
