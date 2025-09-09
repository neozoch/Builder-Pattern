# Task 1
from dataclasses import dataclass

@dataclass(frozen=True)
class Computer:
    cpu: str
    ram_gb: int
    hdd_gb: int
    gpu: str | None = None
    os: str = "Linux"

class ComputerBuilder:
    def __init__(self):
        self._cpu = None
        self._ram_gb = ...

    def cpu(self, name: str):
        self._cpu = name
        return self
    
    ...

    def build(self) -> Computer:
        ...

# Task 2a

class ButtonBefore:
    def __init__(self, height, width, bg_color, text_color, border_color):
        ...

@dataclass(frozen=True)
class Button:
    ...

class ButtonBuilder:
    def __init__(self):
        ...

# Task 2b
    
class ButtonDirector:
    def buildPrimaryButton():
        ...
    
    def buildSecondaryButton():
        ...