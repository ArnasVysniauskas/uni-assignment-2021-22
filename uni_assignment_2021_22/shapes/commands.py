import click

from uni_assignment_2021_22.shapes.indexer import Indexer
from uni_assignment_2021_22.shapes.shapes import SHAPES_MAP, Shape


def remove_command(indexer: Indexer, shapes: list[Shape]):
    id = click.prompt(
        "Please provide the id of the shape", type=click.IntRange(min=0, max_open=True)
    )

    for shape in shapes:
        if shape.id == id:
            shapes.remove(shape)
            indexer.remove_index(id)
            break


def list_command(_: Indexer, shapes: list[Shape]):
    for shape in shapes:
        print(shape)


def create_command(indexer: Indexer, shapes: list[Shape]):
    shape_type = click.prompt(
        "Please provide shape type", type=click.Choice(SHAPES_MAP.keys())
    )

    new_id = indexer.get_new_index()
    shapes.append(SHAPES_MAP[shape_type].create(new_id))


def quit_command(*args):
    print("Thanks for using SHAPES!")
    quit()


COMMANDS_MAP = {
    "create": create_command,
    "list": list_command,
    "remove": remove_command,
    "quit": quit_command,
}
