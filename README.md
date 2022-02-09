# uni-assignment-2021-22

## Task A description

The program emulates virtual dice configured by the user
 - Number of sides is provided by the user
 - Number of throws is provided by the user

## Task B description

The program takes a list of numbers and calculates mean and variance of the list
 - Number list is acquired by user input or file input or random value generator
 - random value generator has to accept three values - number of data elements, start value, end value

## Task C description

The program should provide an interface for creating shapes
 - The code should use inheritance for implementing different shapes
 - Shapes inheritance tree: 
    - Shape
       - Point
          - Circle
             - Cylinder
          - Square
             - Cube
          - Rectangle
 - Interface should allow user to:
    - Create any number of shapes
    - List shapes that were created
    - Remove created shapes

## To start using the applications

Prerequisite:
 - python 3.10 or above
 - poetry

1. Pull the repository from github

1. Initialise the environment
   ```
   poetry env use /usr/local/opt/python@3.10/bin/python3
   ```

1. Connect to the environment
   ```
   source <environment_path>/bin/activate
   ```

1. Install dependencies
   ```
   poetry isntall
   ```

1. Use flag '--help' to get more information about each command
   ```
   python3 applications/dice_throws --help
   python3 applications/mean_variance --help
   python3 applications/shapes --help

   ```