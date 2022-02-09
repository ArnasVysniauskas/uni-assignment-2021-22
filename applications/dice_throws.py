import click

from random import seed, randint

@click.command()
@click.option("--sides", type=click.IntRange(min=1, max_open=True), required=True, help="Number of sides of the dice")
@click.option("--throws", type=click.IntRange(min=1, max_open=True), required=True, help="Number of throws to simulate")
@click.option("--custom-seed", type=int, default=1, help="Pseudo-random generator seed")
def main(sides: int, throws: int, custom_seed: int) -> None:
    result_values: list[int] = []
    seed(custom_seed)

    for _ in range(throws):
        new_value = randint(1, sides)
        result_values.append(new_value)
    
    output_file = open("temp/dice_results.csv", "w")
    output_file.write("\n".join([str(value) for value in result_values]))


if __name__ == "__main__":
    main()