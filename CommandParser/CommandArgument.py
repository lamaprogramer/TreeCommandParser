from typing import Callable, Type, List, Self
from CommandParser.types.ArgumentType import ArgumentType
from CommandParser.Argument import Argument

class CommandArgument(Argument):
    def __init__(self, type: Type[ArgumentType], action: Callable = None, data: list = []):
        self.type = type
        self.data = data
        self.action: Callable = action
        self.children: List[Type[Argument]] = []
    
    def withChild(self, arg: Type[Argument]) -> Self:
        self.children.append(arg)
        return self