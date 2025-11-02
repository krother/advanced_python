from __future__ import annotations


class Planet:
    """
    A location in the space game
    """
    def __init__(self, name:str, description: str):
        self.name = name
        self.description = description
        self.connections: list[Planet] = []

    def add_connection(self, planet):
        """adds another connection"""
        self.connections.append(planet)

    def show_connections(self):
        """
        prints a menu with all connected planets        
        """
        ...
