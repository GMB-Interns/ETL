#!/usr/bin/env python3

# cli_tool.py

import click

@click.group()
def cli():
    pass

@cli.command()
def download_prod():
    # Logic to download data from prod
    click.echo('Data downloaded from prod')

@cli.command()
@click.option('--source', help='Path to downloaded data')
def restore_to_test(source):
    # Logic to restore data to test database from the given source
    click.echo(f'Restored data to test db from {source}')

@cli.command()
@click.option('--destination', help='Path to save the destination configuration')
def configure(destination):
    # Logic to save destination configuration
    click.echo(f'Destination set to {destination}')

@cli.command()
@click.option('--now', is_flag=True, help='Send data immediately')
@click.option('--schedule', help='Schedule data sending. Format: dd-mm-yyyy hh:mm')
def send_data(now, schedule):
    if now:
        # Logic to send data immediately
        click.echo('Data sent immediately')
    elif schedule:
        # Logic to schedule data sending
        click.echo(f'Data scheduled to be sent on {schedule}')

if __name__ == '__main__':
    cli()
