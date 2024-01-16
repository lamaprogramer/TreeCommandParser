from CommandParser.types.ArgumentType import ArgumentType
from typing import Optional

class IntArgumentType(ArgumentType[int]):
    
    def parse(self, value: str) -> Optional[int]:
        try:
            return int(value)
        except ValueError:
            return None

class FloatArgumentType(ArgumentType[float]):
    
    def parse(self, value: str) -> Optional[float]:
        try:
            return float(value)
        except ValueError:
            return None
        
class BoolArgumentType(ArgumentType[bool]):
    
    def parse(self, value: str) -> Optional[bool]:
        try:
            return bool(value)
        except ValueError:
            return None
        
class StringArgumentType(ArgumentType[str]):
    
    def parse(self, value: str) -> Optional[str]:
        return value