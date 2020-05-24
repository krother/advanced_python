# Enumerations

**Enumerations or Enums** are a way to manage strictly defined states.
They avoid ambiguities and accidental bugs when using standard data types.


## Defining an Enum

An `Enum` is defined by calling the `Enum` as a function with the possible states as as a list:

    :::python
    TrafficLight = Enum('TrafficLight', ["RED", "AMBER", "GREEN"])

Alternatively you can define an `Enum` as a subclass, with the possible states as attributes:

    :::python
    from enum import Enum

    class TrafficLight(Enum):
        RED = 1
        AMBER = 2
        GREEN = 3

## Using an Enum

To use the states in an `Enum`, assign it to a state variable:

    :::python
    a = TrafficLight.RED

Then compare values to another state:  

    :::python
    print(a is TrafficLight.GREEN)
    print(a TrafficLight.RED)

## Inspecting Enums

Also try:

    :::python
    print(TrafficLight.RED.name)
    print(TrafficLight.RED == 1)

## Iterating over an Enums

iterating over an Enum gives you all states:

    :::python
    for x in TrafficLight:
        print(x)
