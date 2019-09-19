import click
import urllib3
from jsonplaceholder.services import get_service_by_name

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.command()
@click.option("--entity", prompt="Entity",
              help="The type of entity you want to work with")
@click.option("--action", prompt="Action",
              help="The action you want to execute")
def hello(entity, action):
    """Simple program that execute a request to an API."""
    service = get_service_by_name(entity)
    if service:
        click.echo("Results:")
        click.echo(service.run_action(action))
    else:
        raise click.exceptions.BadOptionUsage("entity", "The value is not valid")


if __name__ == '__main__':
    hello()
