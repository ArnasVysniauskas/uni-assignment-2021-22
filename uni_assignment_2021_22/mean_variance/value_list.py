
from dataclasses import dataclass
from random import seed
import click
from uni_assignment_2021_22.mean_variance.random_float import randfloat

@dataclass(init=True, frozen=True)
class ValueList:
    value_list: list[float]

    @classmethod
    def create(cls, input_type: str) -> "ValueList":
        value_list = []

        match input_type:
            case "file":
                value_list = cls._get_values_from_file()
            case "manual":
                value_list = cls._get_values_manually()
            case "random":
                value_list = cls._get_random_values()
        
        return ValueList(value_list=value_list)

    def _get_values_from_file() -> list[float]:
        input_file = click.prompt("Please enter relative path to the .csv file", type=click.File())
        value_list: list[float] = []

        for line in input_file:
            try:
                value_list.append(int(line))
            except TypeError:
                print("Please provide only floating type numbers in the file.")
                exit()
            except Exception as exception:
                raise exception

        return value_list

    def _get_values_manually() -> list[float]:
        values =  click.prompt("Please provide the list of values (comma separated floats)", type=str)

        try:
            value_list = [float(number) for number in values.split(",")]
        except Exception as exception:
            raise exception

        return value_list 

    def _get_random_values() -> list[float]:
        number_of_values = click.prompt("Please provide the number of values to generate", type=click.IntRange(min=2, max_open=True))
        custom_seed = click.prompt("Please provide the seed for the pseudo-random number generator", type=int)
        start = click.prompt("Please provide the lower bound", type=float)
        end = click.prompt("Please provide the upper bound", type=float)
        
        seed(custom_seed)

        if start > end:
            print("The upper bound has to be smaller than the lower bound")
            exit()

        return [randfloat(start, end) for _ in range(number_of_values)]
    
    @property
    def variance(self) -> float:
        variance = 0
        mean = self.mean

        for n in self.value_list:
            deviation = n - mean
            variance += deviation ** 2
        variance /= len(self.value_list) - 1

        return variance

    @property
    def mean(self) -> float:
        mean = 0

        for n in self.value_list:
            mean += n
        mean /= len(self.value_list)

        return mean

