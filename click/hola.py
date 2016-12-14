import click

@click.group()
def cli():
    pass

@cli.command()
def hola():
    print "Hola"

@cli.group()
def otro():
    pass

@otro.command()
def adios():
    print "Adios"

cli()
