from dataclasses import dataclass

@dataclass
class Fighter:
    name: str
    level:str
    martial_art: str
    id: int = None
