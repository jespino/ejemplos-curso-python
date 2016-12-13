import click
import os

@click.command()
@click.option("--hidden", prompt=True)
@click.argument("path")
def listar(hidden, path):
    try:
        items = os.listdir(path)
    except OSError:
        click.echo("ERROR: El path %s no existe" % path)
    else:
        for item in items:
            print item

if __name__ == '__main__':
    listar()
