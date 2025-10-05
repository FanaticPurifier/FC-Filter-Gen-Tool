"""Command-line interface for FC Filter Gen Tool."""

import click

@click.command()
@click.option('--input', '-i', required=True, type=click.Path(exists=True), help='Input text file with player data')
@click.option('--output', '-o', required=True, type=click.Path(), help='Output file for generated JSON')
def main(input, output):
    # Placeholder for main logic
    click.echo(f"Input file: {input}")
    click.echo(f"Output file: {output}")

if __name__ == "__main__":
    main()