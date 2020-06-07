from dataclasses import dataclass


@dataclass
class Character:
    name: str = ''
    id: int = 1000
    stars: int = 1
    ranks: int = 0
    has_equip: bool = False
