import click

from uni_assignment_2021_22.shapes.commands import COMMANDS_MAP
from uni_assignment_2021_22.shapes.indexer import Indexer
from uni_assignment_2021_22.shapes.shapes import Shape


@click.command()
def main():
    indexer = Indexer()
    shapes: list[Shape] = []

    while True:
        command = click.prompt(
            "What do you want to do next?", type=click.Choice(COMMANDS_MAP.keys())
        )
        COMMANDS_MAP[command](indexer, shapes)


if __name__ == "__main__":
    main()
