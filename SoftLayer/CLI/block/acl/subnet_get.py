"""Retrieves a list of subents that have been assigned to a host."""
# :license: MIT, see LICENSE for more details.

import click
import SoftLayer
from SoftLayer.CLI import environment
from SoftLayer.CLI import exceptions


@click.command()
@click.argument('host_id')
# @click.option('--columns',
#               callback=column_helper.get_formatter(COLUMNS),
#               help='Columns to display. Options: {0}'.format(
#                   ', '.join(column.name for column in COLUMNS)),
#               default=','.join(DEFAULT_COLUMNS))
@environment.pass_env

def cli(env, host_id):
    """Retrieves a list of subents that have been assigned to a host."""
    block_manager = SoftLayer.BlockStorageManager(env.client)

    #Add a check in case the subnet_id_list is empty

    result = block_manager.get_subnets_in_acl(host_id)

    env.fout(result)

    # If no exception was raised, the command succeeded
    click.echo('Retrieving subnets for host ID: %s' % host_id)
