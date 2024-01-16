from abc import ABC, abstractmethod
from typing import TypeVar, Optional, Generic

T = TypeVar("T")
class ArgumentType(Generic[T], ABC):
    
    @abstractmethod
    def parse(value: str) -> Optional[T]:
        pass
    
        