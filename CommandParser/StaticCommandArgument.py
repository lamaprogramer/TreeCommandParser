from typing import Callable, Type
from CommandParser.types.BaseArgumentTypes import StringArgumentType
from CommandParser.CommandArgument import CommandArgument

class StaticCommandArgument(CommandArgument):
    
    def __init__(self, name: str, action: Callable = None, data: list = []):
        super().__init__(StringArgumentType(), action, data)
        self.name = name
        
    def __str__(self):
        return self.name
