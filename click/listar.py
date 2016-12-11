import click
import os

@click.command()
@click.argument("path")
def listar(path, hidden):
    try:
        items = os.listdir(path)
    except OSError:
        click.echo("ERROR: El path %s no existe" % path)
    else:
        for item in items:
            print item

if __name__ == '__main__':
    listar()
