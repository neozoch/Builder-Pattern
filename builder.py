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
        self._ram_gb = 8
        self._hdd_gb = 256
        self._gpu = None
        self._os = "Linux"

    def cpu(self, name: str):
        self._cpu = name
        return self
    
    def ram_gb(self, name: str):
        self._ram_gb = name
        return self
    
    def hdd_gb(self, name: str):
        self._hdd_gb = name
        return self
    
    def gpu(self, name: str):
        self._gpu = name
        return self
    
    def os(self, name: str):
        self._os = name
        return self

    def build(self) -> Computer:
        if not self._cpu:
            raise ValueError("CPU is required.")
        return Computer(self._cpu, self._ram_gb, self._hdd_gb, self._gpu, self._os)

class Director:
    def buildGamingPC():
        return ComputerBuilder().cpu("Ryzen 7").ram_gb(32).hdd_gb(1024).gpu("RTX 5080").os("Windows").build()
    
    def buildWorkstationPC():
        return ComputerBuilder().cpu("i5").ram_gb(32).hdd_gb(512).os("Windows").build()
    
pc = Director.buildGamingPC()
pc = Director.buildWorkstationPC()

pc2 = Computer("Ryzen 7", 32, 1024, "RTX 5080", "Windows")

class ButtonBefore:
    def __init__(self, height, width, bg_color, text_color, border_color):
        ...

@dataclass(frozen=True)
class Button:
    height: int
    width: int
    bg_color: str
    text_color: str
    border_color: str | None = None

class ButtonBuilder:
    def __init__(self):
        self._height = None
        self._width = None
        self._bg_color = "#6161ff"
        self._text_color = "#ffffff"
        self._border_color = None

    def height(self, height: int):
        if self._height > 0:
            self._height = height
        return self
    
    def width(self, width: int):
        if self._width > 0:
            self._width = width
        return self
    
    def bg_color(self, bg_color: str):
        self._bg_color = bg_color
        return self
    
    def text_color(self, text_color: str):
        self._text_color = text_color
        return self
    
    def border_color(self, border_color: str):
        self._border_color = border_color
        return self

    def build(self):
        if not self._height or not self._width:
            raise ValueError("Height and width are required.")
        return Button(self._height, self._width, self._bg_color, self._text_color, self._border_color)
    
class ButtonDirector:
    def buildPrimaryButton():
        return ButtonBuilder().height(25).width(100)
    
    def buildSecondaryButton():
        return ButtonBuilder().height(25).width(100).bg_color("#ffffff").text_color("#6161ff").border_color("#6161ff")