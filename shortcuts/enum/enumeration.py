"""
Enumerations
"""
from enum import Enum


# defining an Enum
class TrafficLight(Enum):
    RED = 1
    AMBER = 2
    GREEN = 3

print(TrafficLight)

# alternative: functional interface
TrafficLight = Enum('TrafficLight', ["RED", "AMBER", "GREEN"])
print(TrafficLight)


# comparing values
print()
print(TrafficLight.RED)
print(TrafficLight.RED.name)
print(TrafficLight.RED == 1)
print(TrafficLight.RED is TrafficLight.GREEN)

crossing = TrafficLight.RED
print(crossing is TrafficLight.RED)


# iterating over items
print()
for tl in TrafficLight:
    print(tl)

