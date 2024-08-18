from enum import Enum

class SpellType(Enum):
    PYROMANCY = 0
    MIRACLE = 1
    SORCERY = 2
    
SpellType = Enum('SpellType', ['PYROMANCY', 'MIRACLE', 'SORCERY'])