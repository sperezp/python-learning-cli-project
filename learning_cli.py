import click
import urllib3
from jsonplaceholder.posts import posts_service


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@click.command()
@click.option("--entity", prompt="Entity (Post):",
              help="The type of entity you want to work with")
@click.option("--action", prompt="Action (GET_ALL):",
              help="The verb you want to use")
def hello(entity, action):
    """Simple program that execute a request to an API."""
    if entity.lower() == "post" and action.lower() == "get_all":
        click.echo("Results:")
        click.echo(posts_service.get_posts())
    else:
        click.echo("Unknown entity or action")


if __name__ == '__main__':
    hello()
