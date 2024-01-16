from CommandParser.CommandArgument import CommandArgument
from CommandParser.StaticCommandArgument import StaticCommandArgument
from typing import List, Callable

class CommandParser:
    def __init__(self, commands: List[StaticCommandArgument]):
        self.commands = commands

    
    def parse(self, args: list):
        root: StaticCommandArgument = None
        
        for cmd in self.commands:
            if cmd.name == args[0]:
                root = cmd
                
        matched = False
        if root:
            stack = [(root, 0, [])]
            runnables: List[List[Callable, list]] = []
            parsedArguments = []
            
            try:
                while stack:
                    currentNode, patternIndex, path = stack.pop()
                    
                    if not currentNode:
                        continue
                    
                    parsedArg = currentNode.type.parse(args[patternIndex])
                    if parsedArg:
                        path.append([currentNode.action, currentNode.data])
                        if patternIndex != 0:
                            parsedArguments.append(parsedArg)
                        patternIndex += 1
                        
                        if patternIndex == len(args) and not currentNode.children:
                            runnables = path
                            matched = True
                            break
                        
                        for i in range(len(currentNode.children) -1, -1, -1):
                            stack.append((currentNode.children[i], patternIndex, path.copy()))
            except IndexError:
                pass
        
        if matched:
            for program in runnables:
                if program[0]:
                    data: list = program[1]
                    
                    if not data:
                        program[0](parsedArguments)
                    else:
                        program[0](parsedArguments, data)
        else:
            print("pattern not matched")