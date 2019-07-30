"""Assigns subnets to a given ACL."""
# :license: MIT, see LICENSE for more details.ß
import click
import SoftLayer
from SoftLayer.CLI import environment
from SoftLayer.CLI import exceptions


@click.command()
@click.argument('host_id')
@click.option('--subnet-id', '-s', multiple=True,  required=True,
              help='The id of one SoftLayer_Hardware to authorize')
@environment.pass_env
def cli(env, host_id, subnet_id):
    """Assigns subnets to a given host"""
    block_manager = SoftLayer.BlockStorageManager(env.client)
    subnet_id_list = list(subnet_id)

    click.echo('Test to spit out %s' % subnet_id_list[0])

    click.echo('\n Test to spit out 2 %s' % type(subnet_id))

    #print out the subnet input to find out what's happening here :O
    #Add a check in case the subnet_id_list is empty

    result = block_manager.assign_subnets_to_acl(host_id, subnet_id_list)

    env.fout(result)

    # If no exception was raised, the command succeeded
    click.echo('Desired subnets added to host with id: %s' % host_id)
