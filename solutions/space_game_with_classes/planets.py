from __future__ import annotations
#__future__ is a special module in Python that lets you use features from future versions of Python — before they become the default behavior.
# annotations makes Python treat type hints as strings (lazy evaluation), allowing forward references.

#TO DO:
#use the code from academis.eu to implement the planet class
# and create the 5 planets from the game here
# run this file 
# optional: implement the show_connections () method 

from text import TEXT
from copy import copy


class Planet:
#classes usually have a name starting with a capital letter
    """
    A location in the space game
    """
    #docstring describing class
    def __init__(self, name:str, description: str, connections: list[Planet] | None = None):
        #constructor method
        #self, reference to the current instance
        #self is used to reference the instance and define variables for the object's attributes
        self.name = name
        self.description : str = description
        self.connections: list[Planet] = connections or []
    
    def __repr__(self) -> str:
        #__repr__ stands for representation.It defines how your object is represented as a string — especially when you print it in the interpreter, debugger, or logs.
        return f"< Planet (name = {self.name}) >"
    
    def __del__(self):
        #A destructor is a special method in Python that is automatically called when an object is about to be destroyed — i.e., when it’s no longer in use and is being cleaned up by Python’s garbage collector.
        print(f"the end for {self.name}")

    def add_connection(self, planet):
        """adds another connection"""
        self.connections.append(planet)

    def show_connections(self):
        """
        prints a menu with all connected planets        
        """
        if not self.connections:
            print(f"{self.name} has no connections yet.")
            return
        
        position = 1
        for d in self.connections:
            print(f"[{position}] {d.name}")
            position += 1

planets = {
    "earth": Planet(name="earth", description=TEXT["EARTH_DESCRIPTION"]),
    "centauri": Planet(name="centauri", description=TEXT["CENTAURI_DESCRIPTION"]),
    "sirius": Planet(name="sirius", description=TEXT["SIRIUS_DESCRIPTION"]),
    "orion": Planet(name="orion", description=TEXT["ORION_DESCRIPTION"]),
    "black_hole": Planet(name="black_hole", description=TEXT["BLACK_HOLE_DESCRIPTION"]),
}

#add connections
planets["earth"].add_connection(planets["centauri"])
planets["earth"].add_connection(planets["sirius"])
planets["centauri"].add_connection(planets["earth"])
planets["centauri"].add_connection(planets["orion"])
planets["orion"].add_connection(planets["centauri"])
planets["orion"].add_connection(planets["sirius"])
planets["sirius"].add_connection(planets["orion"])
planets["sirius"].add_connection(planets["earth"])
planets["sirius"].add_connection(planets["black_hole"])
planets["black_hole"].add_connection(planets["sirius"])


#planets["earth"].show_connections()

#earth = Planet(name="earth", description="blue planet")
#other = copy(earth)

#print(earth)
#print(other)

#can do this but you dont see anything
#earth.__del__()