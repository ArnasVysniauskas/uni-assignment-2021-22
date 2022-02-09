import click

from uni_assignment_2021_22.mean_variance.value_list import ValueList


@click.command()
@click.option("--input-type", type=click.Choice(["file", "manual", "random"]))
def main(input_type: str) -> None:
    value_list = ValueList.create(input_type)

    output_file = open("temp/mean_variance_results.txt", "w")

    output_file.write(f"List: \t\t{value_list.value_list}\n")
    output_file.write(f"Variance: \t{value_list.variance}\n")
    output_file.write(f"Mean: \t\t{value_list.mean}\n")


if __name__ == "__main__":
    main()
